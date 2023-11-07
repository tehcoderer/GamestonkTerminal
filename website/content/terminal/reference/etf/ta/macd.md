---
title: macd
description: Describes the Moving Average Convergence Divergence (MACD), a metric
  used to indicate trend changes and potential buy/sell signals in markets. The page
  includes usage, parameters, and a visual example.
keywords:
- MACD
- Moving Average Convergence Divergence
- Exponential Moving Averages
- Signal line
- trend changes
- overbought conditions
- oversold conditions
- Divergence
- buy signal
- sell signal
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="etf/ta/macd - Reference | OpenBB Terminal Docs" />

The Moving Average Convergence Divergence (MACD) is the difference between two Exponential Moving Averages. The Signal line is an Exponential Moving Average of the MACD. The MACD signals trend changes and indicates the start of new trend direction. High values indicate overbought conditions, low values indicate oversold conditions. Divergence with the price indicates an end to the current trend, especially if the MACD is at extreme high or low values. When the MACD line crosses above the signal line a buy signal is generated. When the MACD crosses below the signal line a sell signal is generated. To confirm the signal, the MACD should be above zero for a buy, and below zero for a sell.

### Usage

```python
macd [--fast N_FAST] [--slow N_SLOW] [--signal N_SIGNAL]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| n_fast | The short period. | 12 | True | None |
| n_slow | The long period. | 26 | True | None |
| n_signal | The signal period. | 9 | True | None |

![macd](https://user-images.githubusercontent.com/46355364/154311220-d18eb93e-76b3-4abb-b9c6-86484f462c55.png)

---