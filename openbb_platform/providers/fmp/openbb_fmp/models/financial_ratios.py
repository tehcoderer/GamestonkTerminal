"""FMP Financial Ratios Model."""

from datetime import datetime
from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.financial_ratios import (
    FinancialRatiosData,
    FinancialRatiosQueryParams,
)
from openbb_core.provider.utils.descriptions import (
    DATA_DESCRIPTIONS,
    QUERY_DESCRIPTIONS,
)
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    ClientSession,
    amake_requests,
    to_snake_case,
)
from pydantic import Field, model_validator


class FMPFinancialRatiosQueryParams(FinancialRatiosQueryParams):
    """FMP Financial Ratios Query.

    Source: https://financialmodelingprep.com/developer/docs/#Company-Financial-Ratios
    """

    __json_schema_extra__ = {"symbol": ["multiple_items_allowed"]}

    period: Literal["annual", "quarter", "ttm"] = Field(
        default="annual", description=QUERY_DESCRIPTIONS.get("period", "")
    )
    with_ttm: Optional[bool] = Field(
        default=False, description="Include trailing twelve months (TTM) data."
    )


class FMPFinancialRatiosData(FinancialRatiosData):
    """FMP Financial Ratios Data."""

    __alias_dict__ = {
        "dividend_yield": "dividend_yiel",
        "dividend_yield_percentage": "dividend_yiel_percentage",
        "period_ending": "date",
        "fiscal_period": "period",
        "fiscal_year": "calendar_year",
    }

    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    current_ratio: Optional[float] = Field(default=None, description="Current ratio.")
    quick_ratio: Optional[float] = Field(default=None, description="Quick ratio.")
    cash_ratio: Optional[float] = Field(default=None, description="Cash ratio.")
    days_of_sales_outstanding: Optional[float] = Field(
        default=None, description="Days of sales outstanding."
    )
    days_of_inventory_outstanding: Optional[float] = Field(
        default=None, description="Days of inventory outstanding."
    )
    operating_cycle: Optional[float] = Field(
        default=None, description="Operating cycle."
    )
    days_of_payables_outstanding: Optional[float] = Field(
        default=None, description="Days of payables outstanding."
    )
    cash_conversion_cycle: Optional[float] = Field(
        default=None, description="Cash conversion cycle."
    )
    gross_profit_margin: Optional[float] = Field(
        default=None, description="Gross profit margin."
    )
    operating_profit_margin: Optional[float] = Field(
        default=None, description="Operating profit margin."
    )
    pretax_profit_margin: Optional[float] = Field(
        default=None, description="Pretax profit margin."
    )
    net_profit_margin: Optional[float] = Field(
        default=None, description="Net profit margin."
    )
    effective_tax_rate: Optional[float] = Field(
        default=None, description="Effective tax rate."
    )
    return_on_assets: Optional[float] = Field(
        default=None, description="Return on assets."
    )
    return_on_equity: Optional[float] = Field(
        default=None, description="Return on equity."
    )
    return_on_capital_employed: Optional[float] = Field(
        default=None, description="Return on capital employed."
    )
    net_income_per_ebt: Optional[float] = Field(
        default=None, description="Net income per EBT."
    )
    ebt_per_ebit: Optional[float] = Field(default=None, description="EBT per EBIT.")
    ebit_per_revenue: Optional[float] = Field(
        default=None, description="EBIT per revenue."
    )
    debt_ratio: Optional[float] = Field(default=None, description="Debt ratio.")
    debt_equity_ratio: Optional[float] = Field(
        default=None, description="Debt equity ratio."
    )
    long_term_debt_to_capitalization: Optional[float] = Field(
        default=None, description="Long term debt to capitalization."
    )
    total_debt_to_capitalization: Optional[float] = Field(
        default=None, description="Total debt to capitalization."
    )
    interest_coverage: Optional[float] = Field(
        default=None, description="Interest coverage."
    )
    cash_flow_to_debt_ratio: Optional[float] = Field(
        default=None, description="Cash flow to debt ratio."
    )
    company_equity_multiplier: Optional[float] = Field(
        default=None, description="Company equity multiplier."
    )
    receivables_turnover: Optional[float] = Field(
        default=None, description="Receivables turnover."
    )
    payables_turnover: Optional[float] = Field(
        default=None, description="Payables turnover."
    )
    inventory_turnover: Optional[float] = Field(
        default=None, description="Inventory turnover."
    )
    fixed_asset_turnover: Optional[float] = Field(
        default=None, description="Fixed asset turnover."
    )
    asset_turnover: Optional[float] = Field(default=None, description="Asset turnover.")
    operating_cash_flow_per_share: Optional[float] = Field(
        default=None, description="Operating cash flow per share."
    )
    free_cash_flow_per_share: Optional[float] = Field(
        default=None, description="Free cash flow per share."
    )
    cash_per_share: Optional[float] = Field(default=None, description="Cash per share.")
    payout_ratio: Optional[float] = Field(default=None, description="Payout ratio.")
    operating_cash_flow_sales_ratio: Optional[float] = Field(
        default=None, description="Operating cash flow sales ratio."
    )
    free_cash_flow_operating_cash_flow_ratio: Optional[float] = Field(
        default=None, description="Free cash flow operating cash flow ratio."
    )
    cash_flow_coverage_ratios: Optional[float] = Field(
        default=None, description="Cash flow coverage ratios."
    )
    short_term_coverage_ratios: Optional[float] = Field(
        default=None, description="Short term coverage ratios."
    )
    capital_expenditure_coverage_ratio: Optional[float] = Field(
        default=None, description="Capital expenditure coverage ratio."
    )
    dividend_paid_and_capex_coverage_ratio: Optional[float] = Field(
        default=None, description="Dividend paid and capex coverage ratio."
    )
    dividend_payout_ratio: Optional[float] = Field(
        default=None, description="Dividend payout ratio."
    )
    price_book_value_ratio: Optional[float] = Field(
        default=None, description="Price book value ratio."
    )
    price_to_book_ratio: Optional[float] = Field(
        default=None, description="Price to book ratio."
    )
    price_to_sales_ratio: Optional[float] = Field(
        default=None, description="Price to sales ratio."
    )
    price_earnings_ratio: Optional[float] = Field(
        default=None, description="Price earnings ratio."
    )
    price_to_free_cash_flows_ratio: Optional[float] = Field(
        default=None, description="Price to free cash flows ratio."
    )
    price_to_operating_cash_flows_ratio: Optional[float] = Field(
        default=None, description="Price to operating cash flows ratio."
    )
    price_cash_flow_ratio: Optional[float] = Field(
        default=None, description="Price cash flow ratio."
    )
    price_earnings_to_growth_ratio: Optional[float] = Field(
        default=None, description="Price earnings to growth ratio."
    )
    price_sales_ratio: Optional[float] = Field(
        default=None, description="Price sales ratio."
    )
    dividend_yield: Optional[float] = Field(default=None, description="Dividend yield.")
    dividend_yield_percentage: Optional[float] = Field(
        default=None, description="Dividend yield percentage."
    )
    dividend_per_share: Optional[float] = Field(
        default=None, description="Dividend per share."
    )
    enterprise_value_multiple: Optional[float] = Field(
        default=None, description="Enterprise value multiple."
    )
    price_fair_value: Optional[float] = Field(
        default=None, description="Price fair value."
    )

    @model_validator(mode="before")
    @classmethod
    def replace_zero(cls, values):  # pylint: disable=no-self-argument
        """Check for zero values and replace with None."""
        return (
            {k: None if v == 0 else v for k, v in values.items()}
            if isinstance(values, dict)
            else values
        )


class FMPFinancialRatiosFetcher(
    Fetcher[
        FMPFinancialRatiosQueryParams,
        List[FMPFinancialRatiosData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPFinancialRatiosQueryParams:
        """Transform the query params."""
        return FMPFinancialRatiosQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPFinancialRatiosQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"

        ttm_dict = {"period": "TTM", "date": datetime.now().strftime("%Y-%m-%d")}

        async def response_callback(
            response: ClientResponse, session: ClientSession
        ) -> List[Dict]:
            results = await response.json()
            symbol = response.url.parts[-1]

            # TTM data
            ttm_url = f"{base_url}/ratios-ttm/{symbol}?&apikey={api_key}"
            if query.with_ttm and (ratios_ttm := await session.get_one(ttm_url)):
                results.insert(
                    0,
                    {"symbol": symbol, **ttm_dict, **ratios_ttm},
                )

            if query.period == "ttm":
                results = [{**ttm_dict, **item} for item in results]

            return results

        endpoint = "ratios" if query.period != "ttm" else "ratios-ttm"

        urls = [
            (f"{base_url}/{endpoint}/{symbol}") for symbol in query.symbol.split(",")
        ]

        kwargs.update(
            params={"period": query.period, "limit": query.limit, "apikey": api_key}
        )

        return await amake_requests(urls, response_callback=response_callback, **kwargs)

    @staticmethod
    def transform_data(
        query: FMPFinancialRatiosQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPFinancialRatiosData]:
        """Return the transformed data."""
        results = []
        for item in data:
            new_item = {to_snake_case(k).replace("ttm", ""): v for k, v in item.items()}

            if new_item.get("period", None) != "TTM":
                new_item.pop("dividend_yiel_percentage", None)

            if len(query.symbol.split(",")) == 1:
                new_item.pop("symbol", None)

            results.append(FMPFinancialRatiosData.model_validate(new_item))

        return results
