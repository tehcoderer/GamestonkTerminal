# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.fundamental_analysis import yahoo_finance_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "1598220000"),
            ("period2", "1635980400"),
        ],
    }


@pytest.mark.vcr
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "func",
    [
        "display_shareholders",
        "display_dividends",
        "display_splits",
        "display_mktcap",
    ],
)
@pytest.mark.vcr
@pytest.mark.record_stdout
def test_call_func(func):
    getattr(yahoo_finance_view, func)(symbol="PM")


@pytest.mark.vcr
def test_display_info():
    yahoo_finance_view.display_info(symbol="TSLA")


@pytest.mark.vcr(record_mode="none")
@pytest.mark.record_stdout
@pytest.mark.parametrize(
    "func, mocked_func",
    [
        ("display_dividends", "get_dividends"),
        ("display_splits", "get_splits"),
    ],
)
def test_call_func_empty_df(func, mocker, mocked_func):
    mocker.patch(
        "openbb_terminal.stocks.fundamental_analysis.yahoo_finance_model."
        + mocked_func,
        return_value=pd.DataFrame(),
    )
    getattr(yahoo_finance_view, func)(symbol="PM")
