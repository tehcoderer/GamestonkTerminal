"""Tests for the SEC fetchers."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_sec.models.cik_map import SecCikMapFetcher
from openbb_sec.models.company_filings import SecCompanyFilingsFetcher
from openbb_sec.models.equity_ftd import SecEquityFtdFetcher
from openbb_sec.models.equity_search import SecEquitySearchFetcher
from openbb_sec.models.etf_holdings import SecEtfHoldingsFetcher
from openbb_sec.models.form_13FHR import SecForm13FHRFetcher
from openbb_sec.models.institutions_search import SecInstitutionsSearchFetcher
from openbb_sec.models.rss_litigation import SecRssLitigationFetcher
from openbb_sec.models.schema_files import SecSchemaFilesFetcher
from openbb_sec.models.sic_search import SecSicSearchFetcher
from openbb_sec.models.symbol_map import SecSymbolMapFetcher

test_credentials = UserService().default_user_settings.credentials.dict()


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            None,
        ],
    }


@pytest.mark.record_http
def test_sec_etf_holdings_fetcher(credentials=test_credentials):
    """Test the SEC ETF Holdings fetcher."""
    params = {"symbol": "TQQQ", "use_cache": False}

    fetcher = SecEtfHoldingsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_sic_search_fetcher(credentials=test_credentials):
    """Test the SEC SIC Search fetcher."""
    params = {"query": "oil", "use_cache": False}

    fetcher = SecSicSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_symbol_map_fetcher(credentials=test_credentials):
    """Test the SEC Symbol Map fetcher."""
    params = {"query": "0000909832"}

    fetcher = SecSymbolMapFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_equity_ftd_fetcher(credentials=test_credentials):
    """Test the SEC Equity FTD fetcher."""
    params = {"symbol": "AAPL", "limit": 1}

    fetcher = SecEquityFtdFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_equity_search_fetcher(credentials=test_credentials):
    """Test the SEC Equity Search fetcher."""
    params = {"query": "trust", "use_cache": False}

    fetcher = SecEquitySearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_company_filings_fetcher(credentials=test_credentials):
    """Test the SEC Company Filings fetcher."""
    params = {"symbol": "AAPL", "type": "10-K", "use_cache": False}

    fetcher = SecCompanyFilingsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_institutions_search_fetcher(credentials=test_credentials):
    """Test the SEC Institutions Search fetcher."""
    params = {"query": "Investment Trust", "use_cache": False}

    fetcher = SecInstitutionsSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_schema_files_fetcher(credentials=test_credentials):
    """Test the SEC Schema Files fetcher."""
    params = {"query": "2022"}

    fetcher = SecSchemaFilesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_rss_litigation_fetcher(credentials=test_credentials):
    """Test the SEC RSS Litigation fetcher."""
    params = {}

    fetcher = SecRssLitigationFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_cik_map_fetcher(credentials=test_credentials):
    """Test the SEC CIK map fetcher."""
    params = {"symbol": "OXY"}

    fetcher = SecCikMapFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_sec_form_13FHR_fetcher(credentials=test_credentials):
    """Test the SEC Form 13FHR fetcher."""
    params = {"symbol": "NVDA"}

    fetcher = SecForm13FHRFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
