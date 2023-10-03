---
title: cash
description: OpenBB Platform Function
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# cash

Cash Flow Statement.

```python wordwrap
cash(symbol: Union[str, List[str]], period: Literal[str] = annual, limit: NonNegativeInt = 12, provider: Literal[str] = fmp)
```

---

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| period | Literal['annual', 'quarter'] | Period of the data to return. | annual | True |
| limit | NonNegativeInt | The number of data entries to return. | 12 | True |
| provider | Literal['fmp', 'polygon', 'yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'fmp' if there is no default. | fmp | True |
</TabItem>

<TabItem value='polygon' label='polygon'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| company_name | str | Name of the company. |  | True |
| company_name_search | str | Name of the company to search. |  | True |
| sic | str | The Standard Industrial Classification (SIC) of the company. |  | True |
| filing_date | date | Filing date of the financial statement. |  | True |
| filing_date_lt | date | Filing date less than the given date. |  | True |
| filing_date_lte | date | Filing date less than or equal to the given date. |  | True |
| filing_date_gt | date | Filing date greater than the given date. |  | True |
| filing_date_gte | date | Filing date greater than or equal to the given date. |  | True |
| period_of_report_date | date | Period of report date of the financial statement. |  | True |
| period_of_report_date_lt | date | Period of report date less than the given date. |  | True |
| period_of_report_date_lte | date | Period of report date less than or equal to the given date. |  | True |
| period_of_report_date_gt | date | Period of report date greater than the given date. |  | True |
| period_of_report_date_gte | date | Period of report date greater than or equal to the given date. |  | True |
| include_sources | bool | Whether to include the sources of the financial statement. |  | True |
| order | Literal['asc', 'desc'] | Order of the financial statement. |  | True |
| sort | Literal['filing_date', 'period_of_report_date'] | Sort of the financial statement. |  | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[CashFlowStatement]
        Serializable results.

    provider : Optional[Literal['fmp', 'polygon', 'yfinance']]
        Provider name.

    warnings : Optional[List[Warning_]]
        List of warnings.

    chart : Optional[Chart]
        Chart object.

    metadata: Optional[Metadata]
        Metadata info about the command execution.
```

---

## Data

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description |
| ---- | ---- | ----------- |
| symbol | str | Symbol to get data for. |
| date | date | Date of the fetched statement. |
| period | str | Reporting period of the statement. |
| cik | int | Central Index Key (CIK) of the company. |
| net_income | int | Net income. |
| depreciation_and_amortization | int | Depreciation and amortization. |
| stock_based_compensation | int | Stock based compensation. |
| deferred_income_tax | int | Deferred income tax. |
| other_non_cash_items | int | Other non-cash items. |
| changes_in_operating_assets_and_liabilities | int | Changes in operating assets and liabilities. |
| accounts_receivables | int | Accounts receivables. |
| inventory | int | Inventory. |
| vendor_non_trade_receivables | int | Vendor non-trade receivables. |
| other_current_and_non_current_assets | int | Other current and non-current assets. |
| accounts_payables | int | Accounts payables. |
| deferred_revenue | int | Deferred revenue. |
| other_current_and_non_current_liabilities | int | Other current and non-current liabilities. |
| net_cash_flow_from_operating_activities | int | Net cash flow from operating activities. |
| purchases_of_marketable_securities | int | Purchases of investments. |
| sales_from_maturities_of_investments | int | Sales and maturities of investments. |
| investments_in_property_plant_and_equipment | int | Investments in property, plant, and equipment. |
| payments_from_acquisitions | int | Acquisitions, net of cash acquired, and other |
| other_investing_activities | int | Other investing activities |
| net_cash_flow_from_investing_activities | int | Net cash used for investing activities. |
| taxes_paid_on_net_share_settlement | int | Taxes paid on net share settlement of equity awards. |
| dividends_paid | int | Payments for dividends and dividend equivalents |
| common_stock_repurchased | int | Payments related to repurchase of common stock |
| debt_proceeds | int | Proceeds from issuance of term debt |
| debt_repayment | int | Payments of long-term debt |
| other_financing_activities | int | Other financing activities, net |
| net_cash_flow_from_financing_activities | int | Net cash flow from financing activities. |
| net_change_in_cash | int | Net increase (decrease) in cash, cash equivalents, and restricted cash |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| reported_currency | str | Reported currency in the statement. |
| filling_date | date | Filling date. |
| accepted_date | datetime | Accepted date. |
| calendar_year | int | Calendar year. |
| change_in_working_capital | int | Change in working capital. |
| other_working_capital | int | Other working capital. |
| common_stock_issued | int | Common stock issued. |
| effect_of_forex_changes_on_cash | int | Effect of forex changes on cash. |
| cash_at_beginning_of_period | int | Cash at beginning of period. |
| cash_at_end_of_period | int | Cash, cash equivalents, and restricted cash at end of period |
| operating_cash_flow | int | Operating cash flow. |
| capital_expenditure | int | Capital expenditure. |
| free_cash_flow | int | Free cash flow. |
| link | str | Link to the statement. |
| final_link | str | Link to the final statement. |
</TabItem>

</Tabs>
