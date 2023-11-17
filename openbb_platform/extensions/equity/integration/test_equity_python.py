"""Python interface integration tests for the equity extension."""
from datetime import time

import pytest
from openbb_core.app.model.obbject import OBBject

# pylint: disable=too-many-lines,redefined-outer-name


# pylint: disable=import-outside-toplevel,inconsistent-return-statements
@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""
    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb

        return openbb.obb


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 12}),
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
            }
        ),
        (
            {
                "provider": "polygon",
                "include_sources": True,
                "order": "asc",
                "sort": "filing_date",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "filing_date": "2022-10-27",
                "filing_date_lt": "2022-11-01",
                "filing_date_lte": "2022-11-01",
                "filing_date_gt": "2022-10-10",
                "filing_date_gte": "2022-10-10",
                "period_of_report_date": "2022-09-24",
                "period_of_report_date_lt": "2022-11-01",
                "period_of_report_date_lte": "2022-11-01",
                "period_of_report_date_gt": "2022-10-10",
                "period_of_report_date_gte": "2022-10-10",
            }
        ),
        (
            {
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "provider": "fmp",
                "cik": "0000320193",
            }
        ),
        (
            {
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "provider": "yfinance",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_balance(params, obb):
    result = obb.equity.fundamental.balance(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "limit": 10}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_balance_growth(params, obb):
    result = obb.equity.fundamental.balance_growth(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"start_date": "2023-11-05", "end_date": "2023-11-10", "provider": "fmp"}),
        ({"start_date": "2023-11-05", "end_date": "2023-11-10", "provider": "nasdaq"}),
    ],
)
@pytest.mark.integration
def test_equity_calendar_dividend(params, obb):
    result = obb.equity.calendar.dividend(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"start_date": "2023-11-05", "end_date": "2023-11-10", "provider": "fmp"}),
    ],
)
@pytest.mark.integration
def test_equity_calendar_split(params, obb):
    result = obb.equity.calendar.split(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"start_date": "2023-11-09", "end_date": "2023-11-10", "provider": "fmp"}),
        ({"start_date": "2023-11-09", "end_date": "2023-11-10", "provider": "nasdaq"}),
    ],
)
@pytest.mark.integration
def test_equity_calendar_earnings(params, obb):
    result = obb.equity.calendar.earnings(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 12}),
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
            }
        ),
        (
            {
                "provider": "polygon",
                "include_sources": True,
                "order": "asc",
                "sort": "filing_date",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "filing_date": "2022-10-27",
                "filing_date_lt": "2022-11-01",
                "filing_date_lte": "2022-11-01",
                "filing_date_gt": "2022-10-10",
                "filing_date_gte": "2022-10-10",
                "period_of_report_date": "2022-09-24",
                "period_of_report_date_lt": "2022-11-01",
                "period_of_report_date_lte": "2022-11-01",
                "period_of_report_date_gt": "2022-10-10",
                "period_of_report_date_gte": "2022-10-10",
            }
        ),
        (
            {
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "provider": "fmp",
                "cik": "0000320193",
            }
        ),
        (
            {
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "provider": "yfinance",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_cash(params, obb):
    result = obb.equity.fundamental.cash(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "limit": 10}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_cash_growth(params, obb):
    result = obb.equity.fundamental.cash_growth(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_management_compensation(params, obb):
    result = obb.equity.fundamental.management_compensation(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_historical_splits(params, obb):
    result = obb.equity.fundamental.historical_splits(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_dividends(params, obb):
    result = obb.equity.fundamental.dividends(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "limit": 50}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_earnings(params, obb):
    result = obb.equity.fundamental.earnings(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_employee_count(params, obb):
    result = obb.equity.fundamental.employee_count(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 30}),
    ],
)
@pytest.mark.integration
def test_equity_estimates_historical(params, obb):
    result = obb.equity.estimates.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 12}),
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
            }
        ),
        (
            {
                "provider": "polygon",
                "include_sources": True,
                "order": "asc",
                "sort": "filing_date",
                "symbol": "AAPL",
                "period": "annual",
                "limit": 12,
                "filing_date": "2022-10-27",
                "filing_date_lt": "2022-11-01",
                "filing_date_lte": "2022-11-01",
                "filing_date_gt": "2022-10-10",
                "filing_date_gte": "2022-10-10",
                "period_of_report_date": "2022-09-24",
                "period_of_report_date_lt": "2022-11-01",
                "period_of_report_date_lte": "2022-11-01",
                "period_of_report_date_gt": "2022-10-10",
                "period_of_report_date_gte": "2022-10-10",
            }
        ),
        (
            {
                "provider": "fmp",
                "symbol": "AAPL",
                "limit": 12,
                "period": "annual",
                "cik": "0000320193",
            }
        ),
        (
            {
                "provider": "yfinance",
                "symbol": "AAPL",
                "limit": 12,
                "period": "annual",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_income(params, obb):
    result = obb.equity.fundamental.income(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"symbol": "AAPL", "limit": 10, "period": "annual"})],
)
@pytest.mark.integration
def test_equity_fundamental_income_growth(params, obb):
    result = obb.equity.fundamental.income_growth(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "symbol": "AAPL",
                "transaction_type": ["P-Purchase"],
                "limit": 10,
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_ownership_insider_trading(params, obb):
    result = obb.equity.ownership.insider_trading(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "symbol": "AAPL",
                "include_current_quarter": True,
                "date": "2021-09-30",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_ownership_institutional(params, obb):
    result = obb.equity.ownership.institutional(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "symbol": "",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "limit": 100,
                "provider": "intrinio",
            }
        ),
        (
            {
                "start_date": "2023-01-01",
                "end_date": "2023-11-01",
                "status": "priced",
                "provider": "nasdaq",
                "is_spo": False,
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_calendar_ipo(params, obb):
    result = obb.equity.calendar.ipo(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 100}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_metrics(params, obb):
    result = obb.equity.fundamental.metrics(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_management(params, obb):
    result = obb.equity.fundamental.management(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_overview(params, obb):
    result = obb.equity.fundamental.overview(**params)
    assert result
    assert isinstance(result, OBBject)


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "date": "2023-01-01", "page": 1}),
    ],
)
@pytest.mark.integration
def test_equity_ownership_major_holders(params, obb):
    result = obb.equity.ownership.major_holders(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_estimates_price_target(params, obb):
    result = obb.equity.estimates.price_target(**params)
    assert result
    assert isinstance(result, OBBject)


@pytest.mark.parametrize(
    "params",
    [({"symbol": "AAPL"})],
)
@pytest.mark.integration
def test_equity_estimates_consensus(params, obb):
    result = obb.equity.estimates.consensus(**params)
    assert result
    assert isinstance(result, OBBject)


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "limit": 12}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_ratios(params, obb):
    result = obb.equity.fundamental.ratios(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "structure": "flat"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_revenue_per_geography(params, obb):
    result = obb.equity.fundamental.revenue_per_geography(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "period": "annual", "structure": "flat"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_revenue_per_segment(params, obb):
    result = obb.equity.fundamental.revenue_per_segment(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "type": "1", "page": 1, "limit": 100, "provider": "fmp"}),
        (
            {
                "symbol": "AAPL",
                "type": "10-K",
                "limit": 100,
                "cik": None,
                "use_cache": False,
                "provider": "sec",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_filings(params, obb):
    result = obb.equity.fundamental.filings(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_ownership_share_statistics(params, obb):
    result = obb.equity.ownership.share_statistics(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "year": 2023}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_transcript(params, obb):
    result = obb.equity.fundamental.transcript(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_compare_peers(params, obb):
    result = obb.equity.compare.peers(**params)
    assert result
    assert isinstance(result, OBBject)


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "adjusted": True,
                "extended_hours": True,
                "month": "2023-01",
                "output_size": "full",
                "provider": "alpha_vantage",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
                "interval": "1m",
            }
        ),
        (
            {
                "adjusted": True,
                "extended_hours": False,
                "output_size": "full",
                "month": "2023-01",
                "provider": "alpha_vantage",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "provider": "cboe",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
                "interval": "1m",
            }
        ),
        (
            {
                "provider": "cboe",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "limit": "30",
                "provider": "fmp",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-01-02",
                "interval": "1m",
            }
        ),
        (
            {
                "limit": "30",
                "provider": "fmp",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "timezone": "UTC",
                "source": "realtime",
                "start_time": time(5, 30, 0),
                "end_time": time(12, 0, 0),
                "provider": "intrinio",
                "symbol": "AAPL",
                "start_date": "2023-06-01",
                "end_date": "2023-06-03",
                "interval": "1h",
            }
        ),
        (
            {
                "timezone": "UTC",
                "source": "realtime",
                "start_time": time(5, 30, 0),
                "end_time": time(12, 0, 0),
                "provider": "intrinio",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "sort": "desc",
                "limit": "49999",
                "adjusted": "True",
                "provider": "polygon",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-01-03",
                "interval": "1m",
            }
        ),
        (
            {
                "sort": "desc",
                "limit": "49999",
                "adjusted": "True",
                "provider": "polygon",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "prepost": False,
                "include": True,
                "adjusted": False,
                "back_adjust": False,
                "ignore_tz": True,
                "provider": "yfinance",
                "symbol": "AAPL",
                "start_date": "2023-06-01",
                "end_date": "2023-06-03",
                "interval": "1h",
            }
        ),
        (
            {
                "prepost": False,
                "include": True,
                "adjusted": False,
                "back_adjust": False,
                "ignore_tz": True,
                "provider": "yfinance",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "provider": "tiingo",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1d",
            }
        ),
        (
            {
                "provider": "tiingo",
                "symbol": "AAPL",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "interval": "1M",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_price_historical(params, obb):
    if params.get("provider") == "alpha_vantage":
        pytest.skip("skipping alpha_vantage")

    result = obb.equity.price.historical(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "limit": 100, "provider": "fmp"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_multiples(params, obb):
    result = obb.equity.fundamental.multiples(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"query": "ebit", "limit": 100, "provider": "intrinio"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_search_financial_attributes(params, obb):
    result = obb.equity.fundamental.search_financial_attributes(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "tag": "ebit",
                "period": "annual",
                "limit": 1000,
                "type": None,
                "start_date": "2013-01-01",
                "end_date": "2023-01-01",
                "sort": "desc",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_financial_attributes(params, obb):
    result = obb.equity.fundamental.financial_attributes(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"query": "AAPL", "is_symbol": True, "provider": "cboe"}),
        ({"query": "Apple", "provider": "sec", "use_cache": False, "is_fund": False}),
        (
            {
                "query": "residential",
                "industry": "REIT",
                "sector": "Real Estate",
                "mktcap_min": None,
                "mktcap_max": None,
                "price_min": None,
                "price_max": None,
                "volume_min": None,
                "volume_max": None,
                "dividend_min": None,
                "dividend_max": None,
                "is_active": True,
                "is_etf": False,
                "beta_min": None,
                "beta_max": None,
                "country": "US",
                "exchange": "nyse",
                "limit": None,
                "provider": "fmp",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_search(params, obb):
    result = obb.equity.search(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "industry": "REIT",
                "sector": "Real Estate",
                "mktcap_min": None,
                "mktcap_max": None,
                "price_min": None,
                "price_max": None,
                "volume_min": None,
                "volume_max": None,
                "dividend_min": None,
                "dividend_max": None,
                "is_active": True,
                "is_etf": False,
                "beta_min": None,
                "beta_max": None,
                "country": "US",
                "exchange": "nyse",
                "limit": None,
                "provider": "fmp",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_screener(params, obb):
    result = obb.equity.screener(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
        ({"source": "iex", "provider": "intrinio", "symbol": "AAPL"}),
        ({"symbol": "AAPL", "provider": "fmp"}),
    ],
)
@pytest.mark.integration
def test_equity_price_quote(params, obb):
    result = obb.equity.price.quote(**params)
    assert result
    assert isinstance(result, OBBject)


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "provider": "cboe"}),
    ],
)
@pytest.mark.integration
def test_equity_profile(params, obb):
    result = obb.equity.profile(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_gainers(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.gainers(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_losers(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.losers(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_active(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.active(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"symbol": "AAPL"})],
)
@pytest.mark.integration
def test_equity_price_performance(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.price.performance(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_undervalued_large_caps(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.undervalued_large_caps(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_undervalued_growth(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.undervalued_growth(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_aggressive_small_caps(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.aggressive_small_caps(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"sort": "desc"})],
)
@pytest.mark.integration
def test_equity_discovery_growth_tech(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.growth_tech(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"limit": 10})],
)
@pytest.mark.integration
def test_equity_discovery_top_retail(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.top_retail(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"limit": 5})],
)
@pytest.mark.integration
def test_equity_discovery_upcoming_release_days(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.upcoming_release_days(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "start_date": None,
                "end_date": None,
                "limit": 10,
                "form_type": None,
                "is_done": None,
                "provider": "fmp",
            }
        ),
        (
            {
                "start_date": "2023-11-06",
                "end_date": "2023-11-07",
                "limit": 50,
                "form_type": "10-Q",
                "is_done": "true",
                "provider": "fmp",
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_discovery_filings(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.discovery.filings(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
        ({"limit": 24, "provider": "sec", "symbol": "AAPL", "skip_reports": 1}),
    ],
)
@pytest.mark.integration
def test_equity_shorts_fails_to_deliver(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.shorts.fails_to_deliver(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"symbol": "AAPL"})],
)
@pytest.mark.integration
def test_equity_shorts_short_volume(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.shorts.short_volume(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"symbol": "AAPL"})],
)
@pytest.mark.integration
def test_equity_shorts_short_interest(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.shorts.short_interest(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "symbol": "CLOV",
                "date": "2023-10-26",
                "provider": "polygon",
                "limit": 1000,
                "timestamp_lte": None,
                "timestamp_gte": None,
                "timestamp_gt": None,
                "timestamp_lt": None,
            }
        ),
        (
            {
                "symbol": "CLOV",
                "provider": "polygon",
                "timestamp_gt": "2023-10-26T15:20:00.000000000-04:00",
                "timestamp_lt": "2023-10-26T15:30:00.000000000-04:00",
                "limit": 5000,
                "timestamp_gte": None,
                "timestamp_lte": None,
                "date": None,
            }
        ),
    ],
)
@pytest.mark.integration
def test_equity_price_nbbo(params, obb):
    result = obb.equity.price.nbbo(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL"}),
        ({"tier": "T1", "is_ats": True, "provider": "finra", "symbol": "AAPL"}),
    ],
)
@pytest.mark.integration
def test_equity_darkpool_otc(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.darkpool.otc(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"provider": "fmp", "market": "EURONEXT"}),
        ({"provider": "polygon"}),
    ],
)
@pytest.mark.integration
def test_equity_market_snapshots(params, obb):
    result = obb.equity.market_snapshots(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [
        ({"symbol": "AAPL", "limit": 5, "provider": "fmp"}),
    ],
)
@pytest.mark.integration
def test_equity_fundamental_historical_eps(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.fundamental.historical_eps(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0


@pytest.mark.parametrize(
    "params",
    [({"provider": "tiingo", "symbol": "AAPL"})],
)
@pytest.mark.integration
def test_equity_fundamental_trailing_dividend_yield(params, obb):
    params = {p: v for p, v in params.items() if v}

    result = obb.equity.fundamental.trailing_dividend_yield(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
