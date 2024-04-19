"""Test the OECD fetchers."""

import datetime

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_oecd.models.composite_leading_indicator import OECDCLIFetcher
from openbb_oecd.models.gdp_forecast import OECDGdpForecastFetcher
from openbb_oecd.models.gdp_nominal import OECDGdpNominalFetcher
from openbb_oecd.models.gdp_real import OECDGdpRealFetcher
from openbb_oecd.models.long_term_interest_rate import OECDLTIRFetcher
from openbb_oecd.models.short_term_interest_rate import OECDSTIRFetcher
from openbb_oecd.models.unemployment import OECDUnemploymentFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.record_http
def test_oecd_nominal_gdp_fetcher(credentials=test_credentials):
    """Test the OECD Nominal GDP fetcher."""
    params = {
        "start_date": datetime.date(2020, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDGdpNominalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecd_real_gdp_fetcher(credentials=test_credentials):
    """Test the OECD Real GDP fetcher."""
    params = {
        "start_date": datetime.date(2020, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }
    fetcher = OECDGdpRealFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecd_forecast_gdp_fetcher(credentials=test_credentials):
    """Test the OECD GDP Forecast fetcher."""
    params = {
        "start_date": datetime.date(2020, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDGdpForecastFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecd_unemployment_fetcher(credentials=test_credentials):
    """Test the OECD Unemployment Rate fetcher."""
    params = {
        "start_date": datetime.date(2023, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDUnemploymentFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecdcli_fetcher(credentials=test_credentials):
    """Test the OECD Composite Leading Indicator fetcher."""
    params = {
        "start_date": datetime.date(2023, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDCLIFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecdstir_fetcher(credentials=test_credentials):
    """Test the OECD Short Term Interest Rate fetcher."""
    params = {
        "start_date": datetime.date(2023, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDSTIRFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_oecdltir_fetcher(credentials=test_credentials):
    """Test the OECD Long Term Interest Rate fetcher."""
    params = {
        "start_date": datetime.date(2023, 1, 1),
        "end_date": datetime.date(2023, 6, 6),
    }

    fetcher = OECDLTIRFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
