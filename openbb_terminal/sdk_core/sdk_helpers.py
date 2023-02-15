"""OpenBB Terminal SDK Helpers."""
import json
from logging import Logger, getLogger
from typing import Any, Callable, Dict, Optional

import dotenv

import openbb_terminal.config_terminal as cfg
from openbb_terminal.base_helpers import load_env_vars, strtobool
from openbb_terminal.core.config.paths import USER_ENV_FILE
from openbb_terminal.rich_config import console
from openbb_terminal.sdk_core.sdk_init import (
    FORECASTING_TOOLKIT_ENABLED,
    FORECASTING_TOOLKIT_WARNING,
    OPTIMIZATION_TOOLKIT_ENABLED,
    OPTIMIZATION_TOOLKIT_WARNING,
)

if not FORECASTING_TOOLKIT_ENABLED and not load_env_vars(
    "OPENBB_DISABLE_FORECASTING_WARNING", strtobool, False
):
    dotenv.set_key(str(USER_ENV_FILE), "OPENBB_DISABLE_FORECASTING_WARNING", "True")
    console.print(FORECASTING_TOOLKIT_WARNING)

if not OPTIMIZATION_TOOLKIT_ENABLED and not load_env_vars(
    "OPENBB_DISABLE_OPTIMIZATION_WARNING", strtobool, False
):
    dotenv.set_key(str(USER_ENV_FILE), "OPENBB_DISABLE_OPTIMIZATION_WARNING", "True")
    console.print(OPTIMIZATION_TOOLKIT_WARNING)


def clean_attr_desc(attr: Optional[Any] = None) -> Optional[str]:
    """Clean the attribute description."""
    if attr.__doc__ is None:
        return None
    return (
        attr.__doc__.splitlines()[1].lstrip()
        if not attr.__doc__.splitlines()[0]
        else attr.__doc__.splitlines()[0].lstrip()
        if attr.__doc__
        else ""
    )


def class_repr(cls_dict: Dict[str, Any]) -> list:
    """Return the representation of the class."""
    return [
        f"    {k}: {clean_attr_desc(v)}\n"
        for k, v in cls_dict.items()
        if v.__doc__ and not k.startswith("_")
    ]


def helptext(func: Callable) -> Callable:
    """Wrapper to preserve the help text of the function."""

    def decorator(f: Callable) -> Callable:
        for attr in [
            "__doc__",
            "__name__",
            "__annotations__",
            "__module__",
            "__defaults__",
            "__kwdefaults__",
            "__dict__",
        ]:
            setattr(f, attr, getattr(func, attr))
        return f

    return decorator


class Category:
    """The base class that all categories must inherit from."""

    _location_path: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize the class"""
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Return the representation of the class."""
        repr_docs = []
        if submodules := class_repr(self.__class__.__dict__):
            repr_docs += ["\nSubmodules:\n"] + submodules
        if attributes := class_repr(self.__dict__):
            repr_docs += ["\nAttributes:\n"] + attributes

        return f"{self.__class__.__name__}(\n{''.join(repr_docs)}\n)"

    def __getattribute__(self, name: str):
        """We override the __getattribute__ method and wrap all callable
        attributes with a wrapper that logs the call and the result.
        """
        if name.startswith("_"):
            return super().__getattribute__(name)

        attr = super().__getattribute__(name)
        trail = f"{self.__class__._location_path}.{name}"

        if callable(attr):

            @helptext(attr)
            def wrapper(*args, **kwargs):
                method = attr

                # We make a copy of the kwargs to avoid modifying the original
                log_kwargs = kwargs.copy()
                log_kwargs["chart"] = "chart" in name

                operation_logger = OperationLogger(
                    trail=trail, method_chosen=method, args=args, kwargs=log_kwargs
                )
                operation_logger.log_before_call()
                method_result = method(*args, **kwargs)
                operation_logger.log_after_call(method_result=method_result)

                return method_result

            return wrapper
        return attr


class OperationLogger:
    last_method: Dict[Any, Any] = {}

    def __init__(
        self,
        trail: str,
        method_chosen: Callable,
        args: Any,
        kwargs: Any,
        logger: Optional[Logger] = None,
    ) -> None:
        self.__trail = trail
        self.__method_chosen = method_chosen
        self.__logger = logger or getLogger(self.__method_chosen.__module__)
        self.__args = args
        self.__kwargs = kwargs

    def log_before_call(
        self,
    ):
        if self.__check_logging_conditions():
            logger = self.__logger
            self.__log_start(logger=logger, method_chosen=self.__method_chosen)
            self.__log_method_info(
                logger=logger,
                trail=self.__trail,
                method_chosen=self.__method_chosen,
                args=self.__args,
                kwargs=self.__kwargs,
            )

    @staticmethod
    def __log_start(logger: Logger, method_chosen: Callable):
        logger.info(
            "START",
            extra={"func_name_override": method_chosen.__name__},
        )

    def __log_method_info(
        self,
        logger: Logger,
        trail: str,
        method_chosen: Callable,
        args: Any,
        kwargs: Any,
    ):
        merged_args = self.__merge_function_args(method_chosen, args, kwargs)
        merged_args = self.__remove_key_and_log_state(
            method_chosen.__module__, merged_args
        )

        logging_info: Dict[str, Any] = {}
        logging_info["INPUT"] = {
            key: str(value)[:100] for key, value in merged_args.items()
        }
        logging_info["VIRTUAL_PATH"] = trail
        logging_info["CHART"] = kwargs.get("chart", False)

        logger.info(
            f"{json.dumps(logging_info)}",
            extra={"func_name_override": method_chosen.__name__},
        )

    @staticmethod
    def __merge_function_args(func: Callable, args: tuple, kwargs: dict) -> dict:
        """
        Merge user input args and kwargs with signature defaults into a dictionary.

        Parameters
        ----------

        func : Callable
            Function to get the args from
        args : tuple
            Positional args
        kwargs : dict
            Keyword args

        Returns
        ----------
        dict
            Merged user args and signature defaults
        """
        import inspect  # pylint: disable=C0415

        sig = inspect.signature(func)
        sig_args = {
            param.name: param.default
            for param in sig.parameters.values()
            if param.default is not inspect.Parameter.empty
        }
        # merge args with sig_args
        sig_args.update(dict(zip(sig.parameters, args)))
        # add kwargs elements to sig_args
        sig_args.update(kwargs)
        return sig_args

    @staticmethod
    def __remove_key_and_log_state(func_module: str, function_args: dict) -> dict:
        """
        Remove API key from the function args and log state of keys.

        Parameters
        ----------
        func_module : str
            Module of the function
        function_args : dict
            Function args

        Returns
        ----------
        dict
            Function args with API key removed
        """

        if func_module == "openbb_terminal.keys_model":
            # pylint: disable=C0415
            from openbb_terminal.core.log.generation.settings_logger import log_keys

            # remove key if defined
            function_args.pop("key", None)
            log_keys()
        return function_args

    def log_after_call(
        self,
        method_result: Any,
    ):
        if self.__check_logging_conditions():
            logger = self.__logger
            self.__log_exception_if_any(
                logger=logger,
                method_result=method_result,
                method_chosen=self.__method_chosen,
            )
            self.__log_end(
                logger=logger,
                method_chosen=self.__method_chosen,
            )
            OperationLogger.last_method = {
                f"{self.__method_chosen.__module__}.{self.__method_chosen.__name__}": {
                    "args": str(self.__args)[:100],
                    "kwargs": str(self.__kwargs)[:100],
                }
            }

    @staticmethod
    def __log_exception_if_any(
        logger: Logger,
        method_chosen: Callable,
        method_result: Any,
    ):
        if isinstance(method_result, Exception):
            logger.exception(
                f"Exception: {method_result}",
                extra={"func_name_override": method_chosen.__name__},
            )

    @staticmethod
    def __log_end(logger: Logger, method_chosen: Callable):
        logger.info(
            "END",
            extra={"func_name_override": method_chosen.__name__},
        )

    def __check_logging_conditions(self) -> bool:
        return not cfg.LOGGING_SUPPRESS and not self.__check_last_method()

    def __check_last_method(self) -> bool:
        current_method = {
            f"{self.__method_chosen.__module__}.{self.__method_chosen.__name__}": {
                "args": str(self.__args)[:100],
                "kwargs": str(self.__kwargs)[:100],
            }
        }
        return OperationLogger.last_method == current_method


def get_sdk_imports_text() -> str:
    """Return the text for the SDK imports."""
    sdk_imports = """\"\"\"OpenBB Terminal SDK.\"\"\"
# flake8: noqa
# pylint: disable=unused-import,wrong-import-order
# pylint: disable=C0302,W0611,R0902,R0903,C0412,C0301,not-callable
import logging

import openbb_terminal.config_terminal as cfg
from openbb_terminal import helper_funcs as helper  # noqa: F401
from openbb_terminal.base_helpers import load_dotenv_and_reload_configs
from openbb_terminal.config_terminal import theme

from openbb_terminal.cryptocurrency.due_diligence.pycoingecko_model import Coin
from openbb_terminal.dashboards.dashboards_controller import DashboardsController
from openbb_terminal.helper_classes import TerminalStyle  # noqa: F401
from openbb_terminal.reports import widget_helpers as widgets  # noqa: F401
from openbb_terminal.reports.reports_controller import ReportController

import openbb_terminal.sdk_core.sdk_init as lib
from openbb_terminal.sdk_core import (
    controllers as ctrl,
    models as model,
)
from openbb_terminal.session.user import User

if User.is_guest():
    load_dotenv_and_reload_configs()

logger = logging.getLogger(__name__)
theme.applyMPLstyle()
\r\r\r
"""
    return "\r".join(sdk_imports.splitlines())
