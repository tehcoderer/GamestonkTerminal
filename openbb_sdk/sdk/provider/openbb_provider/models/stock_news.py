"""Stock News Data Model."""


from datetime import date
from typing import Optional

from pydantic import Field, NonNegativeInt, validator

from openbb_provider.abstract.data import Data, QueryParams
from openbb_provider.metadata import QUERY_DESCRIPTIONS


class StockNewsQueryParams(QueryParams):
    """Stock news query."""

    symbols: str = Field(
        min_length=1, description=QUERY_DESCRIPTIONS.get("symbols", "")
    )
    page: int = Field(
        default=0, description="The page of the stock news to be retrieved."
    )
    limit: Optional[NonNegativeInt] = Field(
        default=15, description="The number of results to return per page."
    )

    @validator("symbols", pre=True)
    def time_validate(cls, v: str):  # pylint: disable=E0213
        return v.upper()


class StockNewsData(Data):
    """Stock News data.

    Returns
    -------
    date : date
        The published date of the news.
    title : str
        The title of the news.
    image : Optional[str]
        The image URL of the news.
    text : str
        The text/body of the news.
    url : str
        The URL of the news.
    """

    date: date
    title: str
    image: Optional[str]
    text: Optional[str]
    url: str