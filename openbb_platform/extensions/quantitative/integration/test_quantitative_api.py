import base64
import json
import random
from typing import Literal

import pytest
import requests
from extensions.tests.conftest import parametrize
from openbb_core.env import Env
from openbb_core.provider.utils.helpers import get_querystring

# pylint:disable=redefined-outer-name

data: dict = {}


def get_headers():
    if "headers" in data:
        return data["headers"]

    userpass = f"{Env().API_USERNAME}:{Env().API_PASSWORD}"
    userpass_bytes = userpass.encode("ascii")
    base64_bytes = base64.b64encode(userpass_bytes)

    data["headers"] = {"Authorization": f"Basic {base64_bytes.decode('ascii')}"}
    return data["headers"]


def request_data(menu: str, symbol: str, provider: str):
    """Randomly pick a symbol and a provider and get data from the selected menu."""
    url = f"http://0.0.0.0:8000/api/v1/{menu}/price/historical?symbol={symbol}&provider={provider}"
    result = requests.get(url, headers=get_headers(), timeout=10)
    return result.json()["results"]


def get_stocks_data():
    if "stocks_data" in data:
        return data["stocks_data"]

    symbol = random.choice(["AAPL", "NVDA", "MSFT", "TSLA", "AMZN", "V"])  # noqa: S311
    provider = random.choice(["fmp", "polygon", "yfinance"])  # noqa: S311

    data["stocks_data"] = request_data("equity", symbol=symbol, provider=provider)
    return data["stocks_data"]


def get_crypto_data():
    if "crypto_data" in data:
        return data["crypto_data"]

    # TODO : add more crypto providers and symbols
    symbol = random.choice(["BTC"])  # noqa: S311
    provider = random.choice(["fmp"])  # noqa: S311

    data["crypto_data"] = request_data(
        menu="crypto",
        symbol=symbol,
        provider=provider,
    )
    return data["crypto_data"]


def get_data(menu: Literal["equity", "crypto"]):
    funcs = {"equity": get_stocks_data, "crypto": get_crypto_data}
    return funcs[menu]()


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close"}, "equity"),
        ({"data": "", "target": "high"}, "crypto"),
    ],
)
@pytest.mark.integration
def test_quantitative_normality(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/normality?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "high"}, "equity"),
        ({"data": "", "target": "high"}, "crypto"),
    ],
)
@pytest.mark.integration
def test_quantitative_capm(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/capm?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "target": "close",
                "threshold_start": "",
                "threshold_end": "",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "target": "high",
                "threshold_start": "0.1",
                "threshold_end": "1.6",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_performance_omega_ratio(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/performance/omega_ratio?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "window": "5", "index": "date"}, "equity"),
        ({"data": "", "target": "high", "window": "10", "index": "date"}, "crypto"),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_kurtosis(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/kurtosis?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "target": "close",
                "fuller_reg": "c",
                "kpss_reg": "ct",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "target": "high",
                "fuller_reg": "ct",
                "kpss_reg": "c",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_unitroot_test(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/unitroot_test?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {"data": "", "target": "close", "rfr": "", "window": "", "index": "date"},
            "equity",
        ),
        (
            {
                "data": "",
                "target": "high",
                "rfr": "0.5",
                "window": "250",
                "index": "date",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_performance_sharpe_ratio(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = (
        f"http://0.0.0.0:8000/api/v1/quantitative/performance/sharpe_ratio?{query_str}"
    )
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "target": "close",
                "target_return": "",
                "window": "",
                "adjusted": "",
                "index": "date",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "target": "close",
                "target_return": "0.5",
                "window": "275",
                "adjusted": "true",
                "index": "date",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_performance_sortino_ratio(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = (
        f"http://0.0.0.0:8000/api/v1/quantitative/performance/sortino_ratio?{query_str}"
    )
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "window": "220", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_skew(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/skew?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "window": "220", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_variance(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/variance?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "window": "220", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_stdev(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/stdev?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "window": "220", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_mean(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/mean?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "target": "close",
                "window": "10",
                "quantile_pct": "",
                "index": "date",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "target": "high",
                "window": "50",
                "quantile_pct": "0.6",
                "index": "date",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_rolling_quantile(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/rolling/quantile?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close"}, "equity"),
        ({"data": "", "target": "high"}, "crypto"),
    ],
)
@pytest.mark.integration
def test_quantitative_summary(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/summary?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


############
# quantitative/stats
############


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_skew(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/skew?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_kurtosis(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/kurtosis?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_mean(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/mean?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_stdev(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/stdev?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        ({"data": "", "target": "close", "index": "date"}, "equity"),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_variance(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/variance?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=60, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@parametrize(
    "params, data_type",
    [
        (
            {
                "data": "",
                "target": "close",
                "quantile_pct": "",
                "index": "date",
            },
            "equity",
        ),
        (
            {
                "data": "",
                "target": "high",
                "quantile_pct": "0.6",
                "index": "date",
            },
            "crypto",
        ),
    ],
)
@pytest.mark.integration
def test_quantitative_stats_quantile(params, data_type):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(get_data(data_type))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/quantitative/stats/quantile?{query_str}"
    result = requests.post(url, headers=get_headers(), timeout=10, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
