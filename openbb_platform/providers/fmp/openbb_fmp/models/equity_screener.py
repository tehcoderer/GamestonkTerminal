"""FMP Equity Screener fetcher."""

from typing import Any, Dict, List, Literal, Optional

import pandas as pd
from openbb_fmp.utils.definitions import EXCHANGES, SECTORS
from openbb_fmp.utils.helpers import create_url, get_data
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.equity_screener import (
    EquityScreenerData,
    EquityScreenerQueryParams,
)
from pydantic import Field


class FMPEquityScreenerQueryParams(EquityScreenerQueryParams):
    """FMP Equity Screener Query Params."""

    __alias_dict__ = {
        "mktcap_min": "marketCapMoreThan",
        "mktcap_max": "marketCapLowerThan",
        "price_min": "priceMoreThan",
        "price_max": "priceLowerThan",
        "beta_min": "betaMoreThan",
        "beta_max": "betaLowerThan",
        "volume_min": "volumeMoreThan",
        "volume_max": "volumeLowerThan",
        "dividend_min": "dividendMoreThan",
        "dividend_max": "dividendLowerThan",
        "is_active": "isActivelyTrading",
        "is_etf": "isEtf",
    }

    mktcap_min: Optional[int] = Field(
        default=None, description="Filter by market cap greater than this value."
    )
    mktcap_max: Optional[int] = Field(
        default=None,
        description="Filter by market cap less than this value.",
    )
    price_min: Optional[float] = Field(
        default=None,
        description="Filter by price greater than this value.",
    )
    price_max: Optional[float] = Field(
        default=None,
        description="Filter by price less than this value.",
    )
    beta_min: Optional[float] = Field(
        default=None,
        description="Filter by a beta greater than this value.",
    )
    beta_max: Optional[float] = Field(
        default=None,
        description="Filter by a beta less than this value.",
    )
    volume_min: Optional[int] = Field(
        default=None,
        description="Filter by volume greater than this value.",
    )
    volume_max: Optional[int] = Field(
        default=None,
        description="Filter by volume less than this value.",
    )
    dividend_min: Optional[float] = Field(
        default=None,
        description="Filter by dividend amount greater than this value.",
    )
    dividend_max: Optional[float] = Field(
        default=None,
        description="Filter by dividend amount less than this value.",
    )
    is_etf: Optional[bool] = Field(
        default=False,
        description="If true, returns only ETFs.",
    )
    is_active: Optional[bool] = Field(
        default=True,
        description="If false, returns only inactive tickers.",
    )
    sector: Optional[SECTORS] = Field(default=None, description="Filter by sector.")
    industry: Optional[str] = Field(default=None, description="Filter by industry.")
    country: Optional[str] = Field(
        default=None, description="Filter by country, as a two-letter country code."
    )
    exchange: Optional[EXCHANGES] = Field(
        default=None, description="Filter by exchange."
    )
    limit: Optional[int] = Field(
        default=50000, description="Limit the number of results to return."
    )


class FMPEquityScreenerData(EquityScreenerData):
    """FMP Equity Screener Data."""

    __alias_dict__ = {
        "name": "companyName",
    }

    market_cap: Optional[int] = Field(
        description="The market cap of ticker.", alias="marketCap", default=None
    )
    sector: Optional[str] = Field(
        description="The sector the ticker belongs to.", default=None
    )
    industry: Optional[str] = Field(
        description="The industry ticker belongs to.", default=None
    )
    beta: Optional[float] = Field(description="The beta of the ETF.", default=None)
    price: Optional[float] = Field(description="The current price.", default=None)
    last_annual_dividend: Optional[float] = Field(
        description="The last annual amount dividend paid.",
        alias="lastAnnualDividend",
        default=None,
    )
    volume: Optional[int] = Field(
        description="The current trading volume.", default=None
    )
    exchange: Optional[str] = Field(
        description="The exchange code the asset trades on.",
        alias="exchangeShortName",
        default=None,
    )
    exchange_name: Optional[str] = Field(
        description="The full name of the primary exchange.",
        alias="exchange",
        default=None,
    )
    country: Optional[str] = Field(
        description="The two-letter country abbreviation where the head office is located.",
        default=None,
    )
    is_etf: Optional[Literal[True, False]] = Field(
        description="Whether the ticker is an ETF.", alias="isEtf", default=None
    )
    actively_trading: Optional[Literal[True, False]] = Field(
        description="Whether the ETF is actively trading.",
        alias="isActivelyTrading",
        default=None,
    )


class FMPEquityScreenerFetcher(
    Fetcher[
        FMPEquityScreenerQueryParams,
        List[FMPEquityScreenerData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPEquityScreenerQueryParams:
        """Transform the query."""
        return FMPEquityScreenerQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPEquityScreenerQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
        url = create_url(
            version=3,
            endpoint="stock-screener",
            api_key=api_key,
            query=query,
            exclude=["query", "is_symbol", "industry"],
        ).replace(" ", "%20")
        return get_data(url, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPEquityScreenerQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPEquityScreenerData]:
        """Return the transformed data."""
        results = pd.DataFrame(data)
        if len(results) == 0:
            return []
        if query.industry:
            results = results[
                results["sector"].str.contains(query.industry, case=False)
                | results["industry"].str.contains(query.industry, case=False)
            ]
        results["companyName"] = results["companyName"].fillna("-").replace("-", "")
        for col in results:
            if results[col].dtype in ("int", "float"):
                results[col] = results[col].fillna(0).replace(0, None)
        return [
            FMPEquityScreenerData.model_validate(d)
            for d in results.sort_values(by="marketCap", ascending=False).to_dict(
                "records"
            )
        ]
