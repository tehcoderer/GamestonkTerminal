---
title: load
description: OpenBB Platform Function
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# load

Futures Historical Price.

```python wordwrap
load(symbol: Union[str, List[str]], start_date: Union[date, str] = None, end_date: Union[date, str] = None, expiration: str = None, provider: Literal[str] = yfinance)
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
| expiration | str | Future expiry date with format YYYY-MM | None | True |
| provider | Literal['yfinance'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'yfinance' if there is no default. | yfinance | True |
</TabItem>

<TabItem value='yfinance' label='yfinance'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| interval | Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'] | Data granularity. | 1d | True |
| period | Literal['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'] | Period of the data to return. | None | True |
| prepost | bool | Include Pre and Post market data. | False | True |
| adjust | bool | Adjust all the data automatically. | True | True |
| back_adjust | bool | Back-adjusted data to mimic true historical prices. | False | True |
</TabItem>

</Tabs>

---

## Returns

```python wordwrap
OBBject
    results : List[FuturesHistorical]
        Serializable results.

    provider : Optional[Literal['yfinance']]
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
| open | float | The open price of the symbol. |
| high | float | The high price of the symbol. |
| low | float | The low price of the symbol. |
| close | float | The close price of the symbol. |
| volume | float | The volume of the symbol. |
</TabItem>

</Tabs>
