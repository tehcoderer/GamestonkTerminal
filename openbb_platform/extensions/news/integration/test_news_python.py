"""Test news extension."""

import pytest
from extensions.tests.conftest import parametrize
from openbb_core.app.model.obbject import OBBject


@pytest.fixture(scope="session")
def obb(pytestconfig):  # pylint: disable=inconsistent-return-statements
    """Fixture to setup obb."""

    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb  # pylint: disable=import-outside-toplevel

        return openbb.obb


# pylint: disable=redefined-outer-name


@parametrize(
    "params",
    [
        (
            {
                "display": "full",
                "date": "2023-01-01",
                "start_date": "2023-01-01",
                "end_date": "2023-06-06",
                "updated_since": 900000,
                "published_since": 900000,
                "sort": "created",
                "order": "desc",
                "isin": "US0378331005",
                "cusip": "037833100",
                "channels": "General",
                "topics": "car",
                "authors": "Benzinga Insights",
                "content_types": "Car",
                "provider": "benzinga",
                "limit": 20,
            }
        ),
        (
            {
                "provider": "fmp",
                "limit": 20,
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "intrinio",
                "limit": 20,
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "biztoc",
                "filter": "tag",
                "tag": "federalreserve",
                "source": "bloomberg",
                "term": "MSFT",
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "tiingo",
                "limit": 30,
                "source": "bloomberg.com",
                "start_date": None,
                "end_date": None,
                "offset": 0,
            }
        ),
    ],
)
@pytest.mark.integration
def test_news_world(params, obb):
    """Test the news world endpoint."""
    result = obb.news.world(**params)
    assert result
    assert isinstance(result, OBBject)


@parametrize(
    "params",
    [
        (
            {
                "display": "full",
                "date": None,
                "start_date": None,
                "end_date": None,
                "updated_since": None,
                "published_since": None,
                "sort": "created",
                "order": "desc",
                "isin": None,
                "cusip": None,
                "channels": "General",
                "topics": "earnings",
                "authors": None,
                "content_types": "headline",
                "provider": "benzinga",
                "symbol": "AAPL,MSFT",
                "limit": 20,
            }
        ),
        (
            {
                "order": "desc",
                "provider": "polygon",
                "symbol": "AAPL",
                "limit": 20,
                "start_date": "2024-01-10",
                "end_date": "2024-01-10",
            }
        ),
        (
            {
                "provider": "fmp",
                "symbol": "AAPL",
                "limit": 20,
                "page": 1,
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "yfinance",
                "symbol": "AAPL",
                "limit": 20,
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "intrinio",
                "symbol": "AAPL",
                "limit": 20,
                "start_date": None,
                "end_date": None,
            }
        ),
        (
            {
                "provider": "tiingo",
                "symbol": "AAPL",
                "limit": 20,
                "source": "bloomberg.com",
                "start_date": None,
                "end_date": None,
                "offset": None,
            }
        ),
        (
            {
                "provider": "tmx",
                "symbol": "RBC",
                "limit": 20,
                "page": 1,
            }
        ),
    ],
)
@pytest.mark.integration
def test_news_company(params, obb):
    """Test the news company endpoint."""
    params = {p: v for p, v in params.items() if v}

    result = obb.news.company(**params)
    assert result
    assert isinstance(result, OBBject)
    assert len(result.results) > 0
