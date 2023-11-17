"""Intrinio Equity historical end of day fetcher."""

from datetime import datetime, time
from typing import Any, Dict, List, Literal, Optional

from dateutil.relativedelta import relativedelta
from openbb_intrinio.utils.helpers import get_data_one
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.equity_historical import (
    EquityHistoricalData,
    EquityHistoricalQueryParams,
)
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS
from openbb_provider.utils.helpers import get_querystring
from pydantic import Field, PrivateAttr, model_validator


class IntrinioEquityHistoricalQueryParams(EquityHistoricalQueryParams):
    """Intrinio Equity historical end of day Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_security_interval_prices_v2
    """

    symbol: str = Field(
        description="A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)."
    )
    interval: Literal[
        "1m", "5m", "10m", "15m", "30m", "60m", "1h", "1d", "1W", "1M", "1Q", "1Y"
    ] = Field(default="1d", description=QUERY_DESCRIPTIONS.get("interval", ""))
    start_time: Optional[time] = Field(
        default=None,
        description="Return intervals starting at the specified time on the `start_date` formatted as 'HH:MM:SS'.",
    )
    end_time: Optional[time] = Field(
        default=None,
        description="Return intervals stopping at the specified time on the `end_date` formatted as 'HH:MM:SS'.",
    )
    timezone: str = Field(
        default="UTC",
        description="Timezone of the data, in the IANA format (Continent/City).",
    )
    source: Optional[Literal["realtime", "delayed", "nasdaq_basic"]] = Field(
        default="realtime", description="The source of the data."
    )
    _interval_size: Literal["1m", "5m", "10m", "15m", "30m", "60m", "1h"] = PrivateAttr(
        default=None
    )
    _frequency: Literal[
        "daily", "weekly", "monthly", "quarterly", "yearly"
    ] = PrivateAttr(default=None)

    # pylint: disable=protected-access
    @model_validator(mode="after")
    @classmethod
    def set_time_params(cls, values: "IntrinioEquityHistoricalQueryParams"):
        """Set the default start & end date and time params for Intrinio API."""
        frequency_dict = {
            "1d": "daily",
            "1W": "weekly",
            "1M": "monthly",
            "1Q": "quarterly",
            "1Y": "yearly",
        }

        if values.interval in ["1m", "5m", "10m", "15m", "30m", "60m", "1h"]:
            values._interval_size = values.interval
        elif values.interval in ["1d", "1W", "1M", "1Q", "1Y"]:
            values._frequency = frequency_dict[values.interval]

        return values


class IntrinioEquityHistoricalData(EquityHistoricalData):
    """Intrinio Equity historical end of day Data."""

    __alias_dict__ = {"date": "time"}

    close_time: Optional[datetime] = Field(
        default=None,
        description="The timestamp that represents the end of the interval span.",
    )
    interval: Optional[str] = Field(
        default=None,
        description="The data time frequency.",
        alias="frequency",
    )
    average: Optional[float] = Field(
        default=None,
        description="Average trade price of an individual equity during the interval.",
    )
    change: Optional[float] = Field(
        default=None,
        description="Change in the price of the symbol from the previous day.",
    )
    intra_period: Optional[bool] = Field(
        default=None,
        description="If true, the equity price represents an unfinished period "
        "(be it day, week, quarter, month, or year), meaning that the close "
        "price is the latest price available, not the official close price "
        "for the period",
        alias="intraperiod",
    )
    adj_open: Optional[float] = Field(
        default=None,
        description="Adjusted open price during the period.",
    )
    adj_high: Optional[float] = Field(
        default=None,
        description="Adjusted high price during the period.",
    )
    adj_low: Optional[float] = Field(
        default=None,
        description="Adjusted low price during the period.",
    )
    adj_close: Optional[float] = Field(
        default=None,
        description="Adjusted closing price during the period.",
    )
    adj_volume: Optional[float] = Field(
        default=None,
        description="Adjusted volume during the period.",
    )
    factor: Optional[float] = Field(
        default=None,
        description="factor by which to multiply equity prices before this "
        "date, in order to calculate historically-adjusted equity prices.",
    )
    split_ratio: Optional[float] = Field(
        default=None,
        description="Ratio of the equity split, if a equity split occurred.",
    )
    dividend: Optional[float] = Field(
        default=None,
        description="Dividend amount, if a dividend was paid.",
    )
    percent_change: Optional[float] = Field(
        default=None,
        description="Percent change in the price of the symbol from the previous day.",
    )
    fifty_two_week_high: Optional[float] = Field(
        default=None,
        description="52 week high price for the symbol.",
    )
    fifty_two_week_low: Optional[float] = Field(
        default=None,
        description="52 week low price for the symbol.",
    )


class IntrinioEquityHistoricalFetcher(
    Fetcher[
        IntrinioEquityHistoricalQueryParams,
        List[IntrinioEquityHistoricalData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioEquityHistoricalQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        if params.get("start_time") is None:
            transformed_params["start_time"] = time(0, 0, 0)

        if params.get("end_time") is None:
            transformed_params["end_time"] = time(23, 59, 59)

        return IntrinioEquityHistoricalQueryParams(**transformed_params)

    # pylint: disable=protected-access
    @staticmethod
    def extract_data(
        query: IntrinioEquityHistoricalQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""

        base_url = f"https://api-v2.intrinio.com/securities/{query.symbol}/prices"

        if query._interval_size:
            base_url += f"/intervals?interval_size={query._interval_size}"
            data_key = "intervals"
        elif query._frequency:
            base_url += f"?frequency={query._frequency}"
            data_key = "stock_prices"

        query_str = get_querystring(
            query.model_dump(by_alias=True), ["symbol", "interval"]
        )
        url = f"{base_url}&{query_str}&api_key={api_key}"

        data = get_data_one(url, **kwargs)
        next_page = data.get("next_page", None)
        data = data.get(data_key, [])

        while next_page:
            query_str = get_querystring(
                query.model_dump(by_alias=True), ["symbol", "interval"]
            )
            url = f"{base_url}&{query_str}&next_page={next_page}&api_key={api_key}"
            temp_data = get_data_one(url, **kwargs)

            next_page = temp_data.get("next_page", None)
            data.extend(temp_data.get(data_key, []))

        return data

    # pylint: disable=unused-argument
    @staticmethod
    def transform_data(
        query: IntrinioEquityHistoricalQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[IntrinioEquityHistoricalData]:
        """Return the transformed data."""
        return [IntrinioEquityHistoricalData.model_validate(d) for d in data]
