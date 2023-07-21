import json
import os
import platform as pl  # I do this so that the import doesn't conflict with the variable name
from pathlib import Path
from typing import List, Literal, Optional

from pydantic import Field, root_validator, validator

from openbb_core.app.constants import (
    HOME_DIRECTORY,
    OPENBB_DIRECTORY,
    SYSTEM_SETTINGS_PATH,
    USER_SETTINGS_PATH,
)
from openbb_core.app.logs.utils.system_utils import get_branch, get_commit_hash
from openbb_core.app.model.abstract.tagged import Tagged


class SystemSettings(Tagged):
    run_in_isolation: bool = Field(
        default=False,
        description="Whether or not to run each command in total isolation.",
        allow_mutation=False,
    )
    dbms_uri: Optional[str] = Field(
        default=None,
        description="Connection URI like : `mongodb://root:example@localhost:27017/`",
        allow_mutation=False,
    )

    # System section
    os: str = Field(default=str(pl.system()), allow_mutation=False)
    python_version: str = Field(default=str(pl.python_version()), allow_mutation=False)
    platform: str = Field(default=str(pl.platform()), allow_mutation=False)

    # OpenBB section
    # TODO: Get the version of the SDK from somewhere that's not pyproject.toml
    version: str = Field(default="4.0.0dev", allow_mutation=False)
    home_directory: str = Field(default=str(HOME_DIRECTORY), allow_mutation=False)
    openbb_directory: str = Field(default=str(OPENBB_DIRECTORY), allow_mutation=False)
    user_settings_path: str = Field(
        default=str(USER_SETTINGS_PATH), allow_mutation=False
    )
    system_settings_path: str = Field(
        default=str(SYSTEM_SETTINGS_PATH), allow_mutation=False
    )

    # Logging section
    logging_app_name: str = Field(default="gst", allow_mutation=False)
    logging_commit_hash: Optional[str] = Field(default=None, allow_mutation=False)
    logging_branch: Optional[str] = Field(default=None, allow_mutation=False)
    logging_frequency: Literal["D", "H", "M", "S"] = Field(
        default="H", allow_mutation=False
    )
    logging_handlers: List[str] = Field(
        default_factory=lambda: ["file"], allow_mutation=False
    )
    logging_rolling_clock: bool = Field(default=False, allow_mutation=False)
    logging_verbosity: int = Field(default=20, allow_mutation=False)
    logging_sub_app: str = Field(default="sdk", allow_mutation=False)
    logging_suppress: bool = Field(default=False, allow_mutation=False)
    log_collect: bool = Field(default=True, allow_mutation=False)

    # Others
    test_mode: bool = False
    debug_mode: bool = False
    headless: bool = False

    class Config:
        validate_assignment = True

    def __repr__(self) -> str:
        return (
            self.__class__.__name__
            + "\n\n"
            + "\n".join([f"{k}: {v}" for k, v in self.dict().items()])
        )

    @staticmethod
    def create_empty_json(path: Path) -> None:
        with open(path, mode="w") as file:
            json.dump({}, file)

    # TODO: Allow setting debug mode from environment variable
    # @root_validator(allow_reuse=True)
    # @classmethod
    # def validate_debug_mode(cls, values):
    #     dm = os.getenv("DEBUG_MODE", "").lower() in ["true", "1"]
    #     values["debug_mode"] = bool(values["debug_mode"] or dm)
    #     return values

    @root_validator(allow_reuse=True)
    @classmethod
    def create_openbb_directory(cls, values):
        obb_dir = values["openbb_directory"]
        user_settings = values["user_settings_path"]
        system_settings = values["system_settings_path"]
        if not os.path.exists(obb_dir):
            os.makedirs(obb_dir)
            cls.create_empty_json(user_settings)
            cls.create_empty_json(system_settings)
        else:
            if not os.path.exists(user_settings):
                cls.create_empty_json(user_settings)
            if not os.path.exists(system_settings):
                cls.create_empty_json(system_settings)
        return values

    @root_validator(allow_reuse=True)
    @classmethod
    def validate_posthog_handler(cls, values):
        if (
            not any([values["test_mode"], values["logging_suppress"]])
            and values["log_collect"]
            and "posthog" not in values["logging_handlers"]
        ):
            values["logging_handlers"].append("posthog")

        return values

    @validator("logging_handlers", allow_reuse=True, always=True)
    @classmethod
    def validate_logging_handlers(cls, v):
        for value in v:
            if value not in ["stdout", "stderr", "noop", "file", "posthog"]:
                raise ValueError("Invalid logging handler")
        return v

    @validator("logging_commit_hash", allow_reuse=True, always=True)
    @classmethod
    def validate_commit_hash(cls, v):
        return v or get_commit_hash()

    @root_validator(allow_reuse=True)
    @classmethod
    def validate_branch(cls, values):
        branch = values["logging_branch"]
        commit_hash = values["logging_commit_hash"]

        if not branch and commit_hash:
            values["logging_branch"] = get_branch(commit_hash)

        return values
