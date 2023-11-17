"""Equity NBBO data model."""

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import QUERY_DESCRIPTIONS


class EquityNBBOQueryParams(QueryParams):
    """Equity NBBO query model."""

    symbol: str = Field(
        description=QUERY_DESCRIPTIONS.get("symbol", ""),
    )

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def upper_symbol(cls, v: str):
        """Convert symbol to uppercase."""
        return v.upper()


class EquityNBBOData(Data):
    """Equity NBBO data."""

    ask_exchange: str = Field(
        description="The exchange ID for the ask.",
    )
    ask: float = Field(
        description="The last ask price.",
    )
    ask_size: int = Field(
        description="""
        The ask size. This represents the number of round lot orders at the given ask price.
        The normal round lot size is 100 shares.
        An ask size of 2 means there are 200 shares available to purchase at the given ask price.
        """,
    )
    bid_size: int = Field(
        description="The bid size in round lots.",
    )
    bid: float = Field(
        description="The last bid price.",
    )
    bid_exchange: str = Field(
        description="The exchange ID for the bid.",
    )
