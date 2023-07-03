import builtins
from dataclasses import MISSING
from inspect import Parameter, _empty, isclass, signature
from json import dumps
from pathlib import Path
from typing import (
    Annotated,
    Any,
    Callable,
    Dict,
    List,
    Type,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)
from uuid import NAMESPACE_DNS, uuid5

import pandas as pd
from starlette.routing import BaseRoute

from openbb_sdk_core.app.router import RouterLoader


class PackageBuilder:
    @staticmethod
    def write_to_package(module_code: str, module_name, extension="py") -> None:
        package_folder = Path(__file__).parent / "package"
        package_path = package_folder / f"{module_name}.{extension}"

        package_folder.mkdir(exist_ok=True)

        with package_path.open("w") as file:
            file.write(module_code)

    @classmethod
    def save_module_map(cls):
        route_map = PathHandler.build_route_map()
        path_list = PathHandler.build_path_list(route_map=route_map)
        module_map = {
            PathHandler.build_module_name(path=path): path for path in path_list
        }
        module_code = dumps(obj=module_map, indent=4)
        module_name = "module_map"
        cls.write_to_package(
            module_code=module_code, module_name=module_name, extension="json"
        )

    @classmethod
    def save_modules(cls):
        route_map = PathHandler.build_route_map()
        path_list = PathHandler.build_path_list(route_map=route_map)

        for path in path_list:
            route = PathHandler.get_route(path=path, route_map=route_map)
            if route is None:
                module_code = ModuleBuilder.build(path=path)
                module_name = PathHandler.build_module_name(path=path)
                cls.write_to_package(module_code=module_code, module_name=module_name)

    @classmethod
    def save_package(cls):
        code = (
            "import warnings\n"
            + "warnings.formatwarning = "
            + "lambda message, category, *args, **kwargs: f'{category.__name__}: {message}'\n"
        )
        cls.write_to_package(module_code=code, module_name="__init__")

    @classmethod
    def build(cls) -> None:
        cls.save_module_map()
        cls.save_modules()
        cls.save_package()


class ModuleBuilder:
    @staticmethod
    def build(path: str) -> str:
        code = ImportDefinition.build(path=path)
        code += ClassDefinition.build(path=path)

        return code


class ImportDefinition:
    @staticmethod
    def filter_hint_type_list(hint_type_list: List[Type]) -> List[Type]:
        new_hint_type_list = []
        for hint_type in hint_type_list:
            if hint_type != _empty and hint_type.__module__ != "builtins":
                new_hint_type_list.append(hint_type)

        new_hint_type_list = list(set(new_hint_type_list))

        return new_hint_type_list

    @classmethod
    def get_function_hint_type_list(cls, func: Callable) -> List[Type]:
        sig = signature(func)
        parameter_map = sig.parameters
        return_type = sig.return_annotation

        hint_type_list = []

        for parameter in parameter_map.values():
            hint_type_list.append(parameter.annotation)

        if return_type:
            hint_type = get_args(get_type_hints(return_type)["item"])[0]
            hint_type_list.append(hint_type)

        hint_type_list = cls.filter_hint_type_list(hint_type_list=hint_type_list)

        return hint_type_list

    @classmethod
    def get_path_hint_type_list(cls, path: str) -> List[Type]:
        route_map = PathHandler.build_route_map()
        path_list = PathHandler.build_path_list(route_map=route_map)
        child_path_list = PathHandler.get_child_path_list(
            path=path, path_list=path_list
        )
        hint_type_list = []
        for child_path in child_path_list:
            route = PathHandler.get_route(path=child_path, route_map=route_map)
            if route:
                function_hint_type_list = cls.get_function_hint_type_list(func=route.endpoint)  # type: ignore
                hint_type_list.extend(function_hint_type_list)

        hint_type_list = list(set(hint_type_list))
        return hint_type_list

    @classmethod
    def build(cls, path: str) -> str:
        hint_type_list = cls.get_path_hint_type_list(path=path)
        code = "# MANUAL IMPORTS"
        code += "\nfrom openbb_sdk_core.app.static.container import Container"
        code += "\nfrom openbb_sdk_core.app.model.command_output import CommandOutput"

        # These imports were not detected before build, so we add them manually.
        # TODO: Find a better way to handle this. This is a temporary solution.
        code += "\nimport openbb_provider"
        code += "\nimport pandas"
        code += "\nimport datetime"
        code += "\nfrom types import NoneType"
        code += "\nimport pydantic"
        code += "\nfrom typing import List, Dict, Union, Optional, Literal"
        code += "\nimport warnings"
        code += "\nfrom openbb_sdk_core.app.utils import df_to_basemodel"
        code += "\nfrom openbb_sdk_core.app.model.abstract.warning import OpenBBWarning"

        module_list = [hint_type.__module__ for hint_type in hint_type_list]
        module_list = list(set(module_list))
        module_list.sort()

        code += "\n\n# AUTO IMPORTS\n"
        for module in module_list:
            code += f"import {module}\n"

        return code


class ClassDefinition:
    @staticmethod
    def build(path: str) -> str:
        class_name = PathHandler.build_module_class(path=path)
        code = f'\nclass {class_name}(Container): # route = "{path}"\n'
        route_map = PathHandler.build_route_map()
        path_list = PathHandler.build_path_list(route_map=route_map)
        child_path_list = PathHandler.get_child_path_list(
            path=path,
            path_list=path_list,
        )
        for child_path in child_path_list:
            route = PathHandler.get_route(path=child_path, route_map=route_map)
            if route:
                code += MethodDefinition.build_command_method(path=route.path, func=route.endpoint)  # type: ignore
            else:
                code += MethodDefinition.build_class_loader_method(path=child_path)

        return code


class MethodDefinition:
    @staticmethod
    def build_class_loader_method(path: str) -> str:
        module_name = PathHandler.build_module_name(path=path)
        class_name = PathHandler.build_module_class(path=path)
        function_name = path.rsplit("/", maxsplit=1)[-1].strip("/")

        code = "    @property\n"
        code += f'    def {function_name}(self):  # route = "{path}"\n'
        code += (
            f"        from openbb_sdk_core.app.static.package import {module_name}\n"
        )
        code += f"        return {module_name}.{class_name}(command_runner_session=self._command_runner_session)\n"

        return code

    @staticmethod
    def get_type(field: Any) -> type:
        field_type = getattr(field, "type", Parameter.empty)
        if isclass(field_type):
            name = field_type.__name__
            if name.startswith("Constrained") and name.endswith("Value"):
                name = name[11:-5].lower()
                return getattr(builtins, name, field_type)
            return field_type
        return field_type

    @staticmethod
    def get_default(field: Any):
        field_default = getattr(field, "default", None)
        if field_default is None or field_default is MISSING:
            return Parameter.empty

        default_default = getattr(field_default, "default", None)
        if default_default is MISSING or default_default is Ellipsis:
            return Parameter.empty

        return default_default

    @staticmethod
    def is_annotated_dc(annotation) -> bool:
        return get_origin(annotation) == Annotated and hasattr(
            annotation.__args__[0], "__dataclass_fields__"
        )

    @staticmethod
    def build_func_params(parameter_map: Dict[str, Parameter]) -> str:
        MAP = {
            "data": pd.DataFrame,
            "start_date": str,
            "end_date": str,
        }

        parameter_map.pop("cc", None)

        formatted: Dict[str, Parameter] = {}

        for name, param in parameter_map.items():
            if name == "extra_params":
                formatted[name] = Parameter(name="kwargs", kind=Parameter.VAR_KEYWORD)

            elif MethodDefinition.is_annotated_dc(param.annotation):
                fields = param.annotation.__args__[0].__dataclass_fields__
                for field_name, field in fields.items():
                    name = field_name
                    type_ = MethodDefinition.get_type(field)
                    default = MethodDefinition.get_default(field)

                    new_type = MAP.get(name, None)
                    updated_type = type_ if new_type is None else Union[type_, new_type]

                    formatted[name] = Parameter(
                        name=name,
                        kind=Parameter.POSITIONAL_OR_KEYWORD,
                        annotation=updated_type,
                        default=default,
                    )
            else:
                new_type = MAP.get(name, None)
                updated_type = (
                    param.annotation
                    if new_type is None
                    else Union[param.annotation, new_type]
                )

                formatted[name] = Parameter(
                    name=name,
                    kind=Parameter.POSITIONAL_OR_KEYWORD,
                    annotation=updated_type,
                    default=param.default,
                )

        func_params = ", ".join(str(param) for param in formatted.values())

        return func_params

    @staticmethod
    def build_func_returns(return_type: type) -> str:
        if return_type == _empty:
            func_returns = "None"
        elif return_type.__module__ == "builtins":
            func_returns = return_type.__name__
        else:
            item_type = get_args(get_type_hints(return_type)["item"])[0]
            if item_type.__module__ == "builtins":
                func_returns = f"CommandOutput[{item_type.__name__}]"
            # elif get_origin(item_type) == list:
            #     inner_type = get_args(item_type)[0]
            #     select = f"[{inner_type.__module__}.{inner_type.__name__}]"
            #     func_returns = f"CommandOutput[{item_type.__module__}.{item_type.__name__}[{select}]]"
            else:
                func_returns = (
                    f"CommandOutput[{item_type.__module__}.{item_type.__name__}]"
                )

        return func_returns

    @staticmethod
    def build_command_method_signature(
        func_name: str, parameter_map: Dict[str, Parameter], return_type: type
    ) -> str:
        func_params = MethodDefinition.build_func_params(parameter_map)
        func_returns = MethodDefinition.build_func_returns(return_type)
        code = f"\n    def {func_name}(self, {func_params}) -> {func_returns}:\n"

        return code

    @staticmethod
    def build_command_method_doc(func: Callable):
        code = f'        """{func.__doc__}"""\n' if func.__doc__ else ""

        return code

    @staticmethod
    def build_command_method_implementation(path: str, func: Callable):
        sig = signature(func)
        parameter_map = dict(sig.parameters)
        parameter_map.pop("cc", None)

        code = ""
        if "data" in parameter_map:
            code += "        if isinstance(data, pandas.DataFrame):\n"
            code += "            data = df_to_basemodel(data, data.index.name is not None)\n"
            code += "\n"

        code += "        o = self._command_runner_session.run(\n"
        code += f"""            "{path}",\n"""

        for name, param in parameter_map.items():
            if name == "extra_params":
                code += f"            {name} = kwargs,\n"
            elif MethodDefinition.is_annotated_dc(param.annotation):
                fields = param.annotation.__args__[0].__dataclass_fields__
                value = {k: k for k in fields}
                code += f"            {name} = {{"
                for k, v in value.items():
                    code += f'"{k}": {v}, '
                code += "},\n"
            else:
                code += f"            {name} = {name},\n"
        code += "        ).output\n"
        code += "\n"
        code += "        if o.warnings:\n"
        code += "            for w in o.warnings:\n"
        code += (
            "                category = __builtins__.get(w.category, OpenBBWarning)\n"
        )
        code += "                warnings.warn(w.message, category)\n"
        code += "\n"
        code += "        if o.error:\n"
        code += "            raise Exception(o.error.message)\n"
        code += "        return o\n"

        return code

    @classmethod
    def build_command_method(cls, path: str, func: Callable) -> str:
        # Name
        func_name = func.__name__

        # Parameters
        sig = signature(func)
        parameter_map = dict(sig.parameters)

        code = cls.build_command_method_signature(
            func_name=func_name,
            parameter_map=parameter_map,
            return_type=sig.return_annotation,
        )
        code += cls.build_command_method_doc(func=func)
        code += cls.build_command_method_implementation(path=path, func=func)

        return code


class PathHandler:
    @staticmethod
    def build_route_map() -> Dict[str, BaseRoute]:
        router = RouterLoader.from_plugins()
        route_map = {route.path: route for route in router.api_router.routes}  # type: ignore

        return route_map

    @staticmethod
    def build_path_list(route_map: Dict[str, BaseRoute]) -> List[str]:
        path_list = []
        for route_path in route_map:
            if route_path not in path_list:
                path_list.append(route_path)

                sub_path_list = route_path.split("/")

                for length in range(len(sub_path_list)):
                    sub_path = "/".join(sub_path_list[:length])
                    if sub_path not in path_list:
                        path_list.append(sub_path)

        return path_list

    @staticmethod
    def get_route(path: str, route_map: Dict[str, BaseRoute]):
        return route_map.get(path, None)

    @staticmethod
    def get_child_path_list(path: str, path_list: List[str]) -> List[str]:
        direct_children = []
        for p in path_list:
            if p.startswith(path):
                path_reminder = p[len(path) :]  # noqa: E203
                if path_reminder.count("/") == 1:
                    direct_children.append(p)

        return direct_children

    @staticmethod
    def hash_path(path: str) -> str:
        return str(uuid5(NAMESPACE_DNS, path)).replace("-", "_")

    @classmethod
    def build_module_name(cls, path: str) -> str:
        return f"MODULE_{cls.hash_path(path=path)}"

    @classmethod
    def build_module_class(cls, path: str) -> str:
        return f"CLASS_{cls.hash_path(path=path)}"