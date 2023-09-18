"""CPI data and query params."""
from datetime import date as dateType
from typing import List, Literal, Optional

from pydantic import Field, field_validator

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS

CPI_COUNTRIES = Literal[
    "australia",
    "austria",
    "belgium",
    "brazil",
    "bulgaria",
    "canada",
    "chile",
    "china",
    "croatia",
    "cyprus",
    "czech_republic",
    "denmark",
    "estonia",
    "euro_area",
    "finland",
    "france",
    "germany",
    "greece",
    "hungary",
    "iceland",
    "india",
    "indonesia",
    "ireland",
    "israel",
    "italy",
    "japan",
    "korea",
    "latvia",
    "lithuania",
    "luxembourg",
    "malta",
    "mexico",
    "netherlands",
    "new_zealand",
    "norway",
    "poland",
    "portugal",
    "romania",
    "russian_federation",
    "slovak_republic",
    "slovakia",
    "slovenia",
    "south_africa",
    "spain",
    "sweden",
    "switzerland",
    "turkey",
    "united_kingdom",
    "united_states",
]

CPI_UNITS = Literal["growth_previous", "growth_same", "index_2015"]

CPI_FREQUENCY = Literal["monthly", "quarter", "annual"]


class CPIQueryParams(QueryParams):
    """CPI query."""

    countries: List[CPI_COUNTRIES] = Field(
        description=QUERY_DESCRIPTIONS.get("countries")
    )
    units: CPI_UNITS = Field(
        default="growth_same", description=QUERY_DESCRIPTIONS.get("units")
    )
    frequency: CPI_FREQUENCY = Field(
        default="monthly", description=QUERY_DESCRIPTIONS.get("frequency")
    )
    harmonized: bool = Field(
        default=False, description="Whether you wish to obtain harmonized data."
    )
    start_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("start_date")
    )
    end_date: Optional[dateType] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("end_date")
    )


class CPIData(Data):
    """CPI data."""

    date: Optional[dateType] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("date")
    )
    realtime_start: Optional[dateType] = Field(
        default=None, description="Date the data was updated."
    )
    realtime_end: Optional[dateType] = Field(
        default=None, description="Date the data was updated."
    )
    value: Optional[float] = Field(default=None, description="Value of the data.")

    @field_validator("value", mode="before")
    @classmethod
    def value_validate(cls, v: str):  # pylint: disable=E0213
        """Validate value."""
        if v == ".":
            return 0.0
        return float(v)
