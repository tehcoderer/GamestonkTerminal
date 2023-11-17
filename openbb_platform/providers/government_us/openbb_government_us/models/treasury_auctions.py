"""US Government Treasury Auctions."""

from datetime import (
    datetime,
    timedelta,
)
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.treasury_auctions import (
    USTreasuryAuctionsData,
    USTreasuryAuctionsQueryParams,
)
from openbb_provider.utils.helpers import get_querystring


class GovernmentUSTreasuryAuctionsQueryParams(USTreasuryAuctionsQueryParams):
    """
    US Treasury Auctions Query Params

    Source: https://www.treasurydirect.gov/
    """

    __alias_dict__ = {
        "start_date": "startDate",
        "end_date": "endDate",
        "security_type": "type",
        "page_size": "pagesize",
        "page_num": "pagenum",
    }


class GovernementUSTreasuryAuctionsData(USTreasuryAuctionsData):
    """US Treasury Auctions Data."""


class GovernmentUSTreasuryAuctionsFetcher(
    Fetcher[
        GovernmentUSTreasuryAuctionsQueryParams,
        List[GovernementUSTreasuryAuctionsData],
    ]
):
    """US Treasury Auctions Fetcher."""

    @staticmethod
    def transform_query(
        params: Dict[str, Any]
    ) -> GovernmentUSTreasuryAuctionsQueryParams:
        """Transform query params."""
        transformed_params = params.copy()
        if "start_date" not in transformed_params:
            transformed_params["start_date"] = (
                datetime.now() - timedelta(days=90)
            ).strftime("%Y-%m-%d")
        if "end_date" not in transformed_params:
            transformed_params["end_date"] = datetime.now().strftime("%Y-%m-%d")
        return GovernmentUSTreasuryAuctionsQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: GovernmentUSTreasuryAuctionsQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Extract the raw data from Treasury Direct API."""

        base_url = "https://www.treasurydirect.gov/TA_WS/securities/search?"

        _query = query.model_dump()
        _query["startDate"] = (
            _query["startDate"].strftime("%m/%d/%Y") if query.start_date else None
        )
        _query["endDate"] = (
            _query["endDate"].strftime("%m/%d/%Y") if _query["endDate"] else None
        )
        query_string = get_querystring(_query, [])

        url = base_url + query_string + "&format=json"
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            raise RuntimeError(r.status_code)
        data = pd.DataFrame(r.json())
        results = data.replace("", None).convert_dtypes().to_dict("records")

        return results

    @staticmethod
    def transform_data(
        query: GovernmentUSTreasuryAuctionsQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[GovernementUSTreasuryAuctionsData]:
        """Transform data into the model"""
        return [GovernementUSTreasuryAuctionsData.model_validate(d) for d in data]
