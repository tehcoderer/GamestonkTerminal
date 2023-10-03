"""yfinance Balance Sheet Fetcher."""


import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.balance_sheet import (
    BalanceSheetData,
    BalanceSheetQueryParams,
)
from openbb_provider.utils.errors import EmptyDataError
from pydantic import field_validator
from yfinance import Ticker


class YFinanceBalanceSheetQueryParams(BalanceSheetQueryParams):
    """yfinance Balance Sheet QueryParams.

    Source: https://finance.yahoo.com/
    """


class YFinanceBalanceSheetData(BalanceSheetData):
    """yfinance Balance Sheet Data."""

    # TODO: Standardize the fields

    @field_validator("date", mode="before", check_fields=False)
    @classmethod
    def date_validate(cls, v):  # pylint: disable=E0213
        """Return datetime object from string."""
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%d %H:%M:%S").date()
        return v


class YFinanceBalanceSheetFetcher(
    Fetcher[
        YFinanceBalanceSheetQueryParams,
        List[YFinanceBalanceSheetData],
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFinanceBalanceSheetQueryParams:
        return YFinanceBalanceSheetQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceBalanceSheetQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        period = "yearly" if query.period == "annual" else "quarterly"  # type: ignore
        data = Ticker(query.symbol).get_balance_sheet(
            as_dict=True, pretty=False, freq=period
        )

        if not data:
            raise EmptyDataError()

        data = [{"date": str(key), **value} for key, value in data.items()]
        # To match standardization
        for d in data:
            d["Symbol"] = query.symbol
        data = json.loads(json.dumps(data))

        return data

    @staticmethod
    def transform_data(
        data: List[Dict],
    ) -> List[YFinanceBalanceSheetData]:
        return [YFinanceBalanceSheetData.model_validate(d) for d in data]