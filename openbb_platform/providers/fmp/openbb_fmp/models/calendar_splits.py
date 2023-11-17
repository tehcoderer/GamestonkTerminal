"""FMP Calendar Splits fetcher."""

from datetime import date
from typing import Any, Dict, List, Optional

from dateutil.relativedelta import relativedelta
from openbb_fmp.utils.helpers import create_url, get_data_many
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.calendar_splits import (
    CalendarSplitsData,
    CalendarSplitsQueryParams,
)


class FMPCalendarSplitsQueryParams(CalendarSplitsQueryParams):
    """FMP Calendar Splits query.

    Source: https://site.financialmodelingprep.com/developer/docs/stock-split-calendar-api/
    """


class FMPCalendarSplitsData(CalendarSplitsData):
    """FMP Calendar Splits data."""


class FMPCalendarSplitsFetcher(
    Fetcher[
        FMPCalendarSplitsQueryParams,
        List[FMPCalendarSplitsData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCalendarSplitsQueryParams:
        """Transform the query params. Start and end dates are set to a 1 year interval."""
        transformed_params = params

        now = date.today()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return FMPCalendarSplitsQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: FMPCalendarSplitsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        query_str = f"from={query.start_date}&to={query.end_date}"
        url = create_url(3, f"stock_split_calendar?{query_str}", api_key)

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPCalendarSplitsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCalendarSplitsData]:
        """Return the transformed data."""
        return [FMPCalendarSplitsData.model_validate(d) for d in data]
