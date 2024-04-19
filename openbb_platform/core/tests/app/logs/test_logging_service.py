"""Test LoggingService class."""

import json
from typing import Optional
from unittest.mock import MagicMock, Mock, patch

import pytest
from openbb_core.app.logs.logging_service import LoggingService
from openbb_core.app.model.abstract.error import OpenBBError
from pydantic import BaseModel

# ruff: noqa: S106
# pylint: disable=redefined-outer-name, protected-access


class MockLoggingSettings:
    """Mock logging settings."""

    def __init__(self, system_settings, user_settings):
        """Initialize the mock logging settings."""
        self.system_settings = system_settings
        self.user_settings = user_settings


class MockOBBject(BaseModel):
    """Mock object for testing."""

    output: Optional[str] = None
    error: Optional[str] = None


@pytest.fixture(scope="function")
def logging_service():
    """Return a LoggingService instance."""
    mock_system_settings = Mock()
    mock_user_settings = Mock()
    mock_setup_handlers = Mock()
    mock_log_startup = Mock()

    with patch(
        "openbb_core.app.logs.logging_service.LoggingSettings",
        MockLoggingSettings,
    ), patch(
        "openbb_core.app.logs.logging_service.LoggingService._setup_handlers",
        mock_setup_handlers,
    ), patch(
        "openbb_core.app.logs.logging_service.LoggingService._log_startup",
        mock_log_startup,
    ):
        _logging_service = LoggingService(
            system_settings=mock_system_settings,
            user_settings=mock_user_settings,
        )

        return _logging_service


def test_correctly_initialized():
    """Test the LoggingService is correctly initialized."""
    mock_system_settings = Mock()
    mock_user_settings = Mock()
    mock_setup_handlers = Mock()
    mock_log_startup = Mock()

    with patch(
        "openbb_core.app.logs.logging_service.LoggingSettings",
        MockLoggingSettings,
    ), patch(
        "openbb_core.app.logs.logging_service.LoggingService._setup_handlers",
        mock_setup_handlers,
    ), patch(
        "openbb_core.app.logs.logging_service.LoggingService._log_startup",
        mock_log_startup,
    ):
        LoggingService(
            system_settings=mock_system_settings,
            user_settings=mock_user_settings,
        )

        mock_setup_handlers.assert_called_once()
        mock_log_startup.assert_called_once()


def test_logging_settings_setter(logging_service):
    """Test the logging_settings setter."""
    custom_user_settings = "custom_user_settings"
    custom_system_settings = "custom_system_settings"

    with patch(
        "openbb_core.app.logs.logging_service.LoggingSettings",
        MockLoggingSettings,
    ):
        logging_service.logging_settings = (
            custom_system_settings,
            custom_user_settings,
        )

    assert logging_service.logging_settings.system_settings == "custom_system_settings"  # type: ignore[attr-defined]
    assert logging_service.logging_settings.user_settings == "custom_user_settings"  # type: ignore[attr-defined]


def test_log_startup(logging_service):
    """Test the log_startup method."""
    with patch("logging.getLogger") as mock_get_logger:
        mock_info = mock_get_logger.return_value.info

        class MockCredentials(BaseModel):
            username: str
            password: str

        logging_service._user_settings = MagicMock(
            preferences="your_preferences",
            credentials=MockCredentials(username="username", password="password"),
        )
        logging_service._system_settings = "your_system_settings"

        logging_service._log_startup(
            route="test_route", custom_headers={"X-OpenBB-Test": "test"}
        )

        expected_log_data = {
            "route": "test_route",
            "PREFERENCES": "your_preferences",
            "KEYS": {
                "username": "defined",
                "password": "defined",  # pragma: allowlist secret
            },
            "SYSTEM": "your_system_settings",
            "custom_headers": {"X-OpenBB-Test": "test"},
        }
        mock_info.assert_called_once_with(
            "STARTUP: %s ",
            json.dumps(expected_log_data),
        )
        mock_get_logger.assert_called_once()


@pytest.mark.parametrize(
    "user_settings, system_settings, route, func, kwargs, exec_info, custom_headers",
    [
        (
            "mock_settings",
            "mock_system",
            "mock_route",
            "mock_func",
            {},
            None,
            None,
        ),
        (
            "mock_settings",
            "mock_system",
            "mock_route",
            "mock_func",
            {},
            (OpenBBError, OpenBBError("mock_error")),
            {"X-OpenBB-Test": "test"},
        ),
        (
            "mock_settings",
            "mock_system",
            "login",
            "mock_func",
            {},
            None,
            {"X-OpenBB-Test1": "test1", "X-OpenBB-Test2": "test2"},
        ),
    ],
)
def test_log(
    logging_service,
    user_settings,
    system_settings,
    route,
    func,
    kwargs,
    exec_info,
    custom_headers,
):
    """Test the log method."""
    with patch(
        "openbb_core.app.logs.logging_service.LoggingSettings",
        MockLoggingSettings,
    ), patch("logging.getLogger") as mock_get_logger:
        if route == "login":
            with patch(
                "openbb_core.app.logs.logging_service.LoggingService._log_startup"
            ) as mock_log_startup:
                logging_service.log(
                    user_settings=user_settings,
                    system_settings=system_settings,
                    route=route,
                    func=func,
                    kwargs=kwargs,
                    exec_info=exec_info,
                    custom_headers=custom_headers,
                )
                mock_log_startup.assert_called_once()

        else:
            mock_info = mock_get_logger.return_value.info
            mock_error = mock_get_logger.return_value.error

            mock_callable = Mock()
            mock_callable.__name__ = func

            logging_service.log(
                user_settings=user_settings,
                system_settings=system_settings,
                route=route,
                func=mock_callable,
                kwargs=kwargs,
                exec_info=exec_info,
                custom_headers=custom_headers,
            )

            message_label = "ERROR" if exec_info else "CMD"
            log_message = json.dumps(
                {
                    "route": route,
                    "input": kwargs,
                    "error": str(exec_info[1]) if exec_info else None,
                    "custom_headers": custom_headers,
                }
            )
            log_message = f"{message_label}: {log_message}"

            if exec_info:
                mock_error.assert_called_once_with(
                    log_message,
                    extra={"func_name_override": "mock_func"},
                    exc_info=exec_info,
                )
            else:
                mock_info.assert_called_once_with(
                    log_message,
                    extra={"func_name_override": "mock_func"},
                    exc_info=exec_info,
                )
