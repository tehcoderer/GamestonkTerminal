---
title: earning
description: OpenBB Platform Function
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# earning

Earnings Calendar.

```python wordwrap
earning(symbol: Union[str, List[str]], limit: int = 50, provider: Literal[str] = fmp)
```

---

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| limit | int | The number of data entries to return. | 50 | True |
| provider | Literal['fmp'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'fmp' if there is no default. | fmp | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[EarningsCalendar]
        Serializable results.

    provider : Optional[Literal['fmp']]
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
| date | date | The date of the data. |
| eps | NonNegativeFloat | EPS of the earnings calendar. |
| eps_estimated | NonNegativeFloat | Estimated EPS of the earnings calendar. |
| time | str | Time of the earnings calendar. |
| revenue | int | Revenue of the earnings calendar. |
| revenue_estimated | int | Estimated revenue of the earnings calendar. |
| updated_from_date | date | Updated from date of the earnings calendar. |
| fiscal_date_ending | date | Fiscal date ending of the earnings calendar. |
</TabItem>

</Tabs>
