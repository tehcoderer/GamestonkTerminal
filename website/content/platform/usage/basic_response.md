---
title: Basic Response & Command Coverage
sidebar_position: 4
description: This page details the basic response and output that can be expected to be received from the the OpenBB Platform, as well as instructions for determining the command coverage provided by the installed extensions.
keywords:
- standardized output
- OBBject
- basic response
- provider
- results
- warnings
- chart
- extra
- command coverage
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Basic Response - Usage | OpenBB Platform Docs" />

The output of every command is an object which contains the results of the request, along with additional information. It is a custom class, `OBBject`, and always returns with the fields listed below:

```console
id: ...                 # UUID Tag
results: ...            # Serializable results.
provider: ...           # Provider name.
warnings: ...           # List of warnings.
chart: ...              # Chart object.
extra: ...              # Extra info.
```

```python
from openbb import obb

data = obb.equity.price.historical("SPY", provider="polygon")

data
```

```console
OBBject

id: 06520558-d54a-7e53-8000-7aafc8a42694
results: [{'date': datetime.datetime(2022, 10, 5, 0, 0), 'open': 375.62, 'high': 37...
provider: polygon
warnings: None
chart: None
extra: {'metadata': {'arguments': {'provider_choices': {'provider': 'polygon'}, 'st...
```

Additional class methods are helpers for converting the results to a variety of formats.

- `to_dict()`: converts to a dictionary, accepting all standard "orientation" parameters, i.e., "records"
- `to_df()` / `to_dataframe()`: converts to a Pandas DataFrame.
- `to_numpy()`: converts to a Numpy array.
- `to_polars()`: converts to a Polars table.

The output from the Fast API is a serialized version of this object, and these methods are lost on conversion.  OBBject can be reconstructed to recover the helpers by importing the model and validating the data.

```python
import requests
from openbb_core.app.model.obbject import OBBject

data = []
symbol="SPY"
url = f"http://127.0.0.1:8000/api/v1/equity/price/historical?provider=polygon&symbol={symbol}"
headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, timeout=3)

if response.status_code == 200:
  data = OBBject.model_validate(response.json())

data.to_df()
```

:::info
The preferred output type can be set with a user preference.

```python
obb.user.preferences.output_type="dataframe"
```
:::

## Dynamic Command Execution

Dynamic execution provides an alternate entry point to functions. This method requires formatting the query as demonstrated below.

```python
from openbb_core.app.command_runner import CommandRunner
runner = CommandRunner()
output = await runner.run(
    "/equity/fundamental/ratios",
    provider_choices={
        "provider": "fmp",
    },
    standard_params={
        "symbol" : "TSLA",
        "period" : "quarter",
    },
    extra_params={}
)
```

```console
>>> output
OBBject

id: 065241b7-bd9d-7313-8000-9406d8afab75
results: [{'symbol': 'TSLA', 'date': '2023-06-30', 'period': 'Q2', 'current_ratio':...
provider: fmp
warnings: None
chart: None
extra: {'metadata': {'arguments': {'provider_choices': {'provider': 'fmp'}, 'standa...
```

## Commands and Provider Coverage

The installed commands and data providers are found under, `obb.coverage`.

```python
obb.coverage
```

```console
/coverage

    providers
    commands
    command_model
    command_schemas
```

`obb.coverage.providers` is a dictionary of the installed provider extensions, each with its own list of available commands.

`obb.coverage.commands` is a dictionary of commands, each with its own list of available providers for the data.

`obb.coverage.command_model` is a dictionary where the keys are the command paths and the values is a nested dictionary of QueryParams and Data models associated with that function.
