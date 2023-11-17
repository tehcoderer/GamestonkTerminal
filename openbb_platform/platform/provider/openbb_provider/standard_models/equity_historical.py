"""Equity Historical Price data model."""


from datetime import (
    date as dateType,
    datetime,
)
from typing import List, Optional, Set, Union

from dateutil import parser
from pydantic import Field, PositiveFloat, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS


class EquityHistoricalQueryParams(QueryParams):
    """Equity Historical end of day Query."""

    symbol: str = Field(description=QUERY_DESCRIPTIONS.get("symbol", ""))
    interval: Optional[str] = Field(
        default="1d",
        description=QUERY_DESCRIPTIONS.get("interval", ""),
    )
    start_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("start_date", ""),
    )
    end_date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("end_date", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: Union[str, List[str], Set[str]]):
        """Convert symbol to uppercase."""
        if isinstance(v, str):
            return v.upper()
        return ",".join([symbol.upper() for symbol in list(v)])


class EquityHistoricalData(Data):
    """Equity Historical end of day price Data."""

    date: datetime = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    open: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("open", ""))
    high: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("high", ""))
    low: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("low", ""))
    close: PositiveFloat = Field(description=DATA_DESCRIPTIONS.get("close", ""))
    volume: Union[float, int] = Field(description=DATA_DESCRIPTIONS.get("volume", ""))
    vwap: Optional[PositiveFloat] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("vwap", "")
    )

    @field_validator("date", mode="before", check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return formatted datetime."""
        return parser.isoparse(str(v))
