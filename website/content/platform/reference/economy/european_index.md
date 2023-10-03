---
title: european_index
description: OpenBB Platform Function
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# european_index

Get historical close values for select European indices.

```python wordwrap
european_index(symbol: Union[str, List[str]], start_date: Union[date, str] = None, end_date: Union[date, str] = None, provider: Literal[str] = cboe)
```

---

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| symbol | Union[str, List[str]] | Symbol to get data for. |  | False |
| start_date | Union[date, str] | Start date of the data, in YYYY-MM-DD format. | None | True |
| end_date | Union[date, str] | End date of the data, in YYYY-MM-DD format. | None | True |
| provider | Literal['cboe'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'cboe' if there is no default. | cboe | True |
</TabItem>

<TabItem value='cboe' label='cboe'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| interval | Literal['1d', '1m'] | Use interval, 1m, for intraday prices during the most recent trading period. | 1d | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[EuropeanIndexHistorical]
        Serializable results.

    provider : Optional[Literal['cboe']]
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
| date | datetime | The date of the data. |
| close | float | The close price of the symbol. |
</TabItem>

<TabItem value='cboe' label='cboe'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| open | float | Opening price for the interval. Only valid when interval is 1m. |
| high | float | High price for the interval. Only valid when interval is 1m. |
| low | float | Low price for the interval. Only valid when interval is 1m. |
| utc_datetime | datetime | UTC datetime. Only valid when interval is 1m. |
</TabItem>

</Tabs>
