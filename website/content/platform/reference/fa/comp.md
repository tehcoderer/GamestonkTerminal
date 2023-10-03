---
title: comp
description: OpenBB Platform Function
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# comp

Executive Compensation.

```python wordwrap
comp(symbol: Union[str, List[str]], provider: Literal[str] = fmp)
```

---

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| provider | Literal['fmp'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'fmp' if there is no default. | fmp | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[ExecutiveCompensation]
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
| cik | str | Central Index Key (CIK) of the company. |
| filing_date | date | Date of the filing. |
| accepted_date | datetime | Date the filing was accepted. |
| name_and_position | str | Name and position of the executive. |
| year | int | Year of the compensation. |
| salary | PositiveFloat | Salary of the executive. |
| bonus | NonNegativeFloat | Bonus of the executive. |
| stock_award | NonNegativeFloat | Stock award of the executive. |
| incentive_plan_compensation | NonNegativeFloat | Incentive plan compensation of the executive. |
| all_other_compensation | NonNegativeFloat | All other compensation of the executive. |
| total | PositiveFloat | Total compensation of the executive. |
| url | str | URL of the filing data. |
</TabItem>

</Tabs>
