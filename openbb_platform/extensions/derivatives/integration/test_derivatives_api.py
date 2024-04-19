"""API integration tests for the derivatives extension."""

import base64

import pytest
import requests
from extensions.tests.conftest import parametrize
from openbb_core.env import Env
from openbb_core.provider.utils.helpers import get_querystring

# pylint: disable=too-many-lines,redefined-outer-name


@pytest.fixture(scope="session")
def headers():
    """Get the headers for the API request."""
    userpass = f"{Env().API_USERNAME}:{Env().API_PASSWORD}"
    userpass_bytes = userpass.encode("ascii")
    base64_bytes = base64.b64encode(userpass_bytes)

    return {"Authorization": f"Basic {base64_bytes.decode('ascii')}"}


@parametrize(
    "params",
    [
        ({"provider": "intrinio", "symbol": "AAPL", "date": "2023-01-25"}),
        ({"provider": "cboe", "symbol": "AAPL", "use_cache": False}),
        ({"provider": "tradier", "symbol": "AAPL"}),
        (
            {
                "provider": "tmx",
                "symbol": "SHOP",
                "date": "2022-12-28",
                "use_cache": False,
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_options_chains(params, headers):
    """Test the options chains endpoint."""
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/options/chains?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params",
    [
        (
            {
                "symbol": "AAPL",
                "provider": "intrinio",
                "start_date": "2023-11-20",
                "end_date": None,
                "min_value": None,
                "max_value": None,
                "trade_type": None,
                "sentiment": "neutral",
                "limit": 1000,
                "source": "delayed",
            }
        )
    ],
)
@pytest.mark.integration
def test_derivatives_options_unusual(params, headers):
    """Test the unusual options endpoint."""
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/options/unusual?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params",
    [
        (
            {
                "provider": "yfinance",
                "interval": "1d",
                "symbol": "CL,BZ",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "expiration": "2025-12",
            }
        ),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_historical(params, headers):
    """Test the futures historical endpoint."""
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/futures/historical?{query_str}"
    result = requests.get(url, headers=headers, timeout=10)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params",
    [
        ({"provider": "cboe", "symbol": "VX", "date": None}),
        ({"provider": "yfinance", "symbol": "ES", "date": "2023-08-01"}),
    ],
)
@pytest.mark.integration
def test_derivatives_futures_curve(params, headers):
    """Test the futures curve endpoint."""
    params = {p: v for p, v in params.items() if v}

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/derivatives/futures/curve?{query_str}"
    result = requests.get(url, headers=headers, timeout=60)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
