---
title: User Settings & Environment Variables
sidebar_position: 3
description: This section details configuring the OpenBB Platform settings and environment variables.
keywords:
- OpenBB Platform
- Python client
- getting started
- OpenBB Hub
- local environment
- environment variables
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="User Settings & Environment Variables - Usage | OpenBB Platform Docs" />

This page outlines configuring the OpenBB Platform with user settings and environment variables.

## User Settings

User preferences are stored locally, `~/.openbb_platform/`, as a JSON file, `user_settings.json`.  It is read upon initializing the Python client, or when the Fast API is authorized. If the file does not exist, it will be created on the first run.

| **Preference**        | **Default**                      | **Options**            | **Description** |
|-----------------------|----------------------------------|------------------------|---------------|
| data_directory        | /home/OpenBBUserData             | Any path.              | When launching the application for the first time  this directory will be created. It serves as the default location where the application stores usage artifacts  such as logs and exports. |
| export_directory      | /home/OpenBBUserData/exports     | Any path.              | The OpenBB Charting Extension provides the capability to export images in various formats. This is the directory where it attempts to save such exports.  |
| cache_directory | /home/OpenBBUserData/cache | Any path.              | The directory where http requests and database caches are stored, for functions with caching. |
| user_styles_directory | /home/OpenBBUserData/styles/user | Any path.              | The OpenBB Charting Extension supports custom stylization. This directory is the location where it looks for user-defined styles. If no user styles are found in this directory  the application will proceed with the default styles.  |
| charting_extension    | openbb_charting                  | ["openbb_charting"] | Name of the charting extension to be used with the application.  |
| chart_style           | dark                             | ["dark", "light"]    | The default color style to use with the OpenBB Charting Extension plots. Options include "dark" and "light".  |
| plot_enable_pywry     | True                             | [True, False]        | Whether the application should enable PyWry. If PyWry is disabled  the image will open in your default browser  otherwise  it will be displayed within your editor or in a separate PyWry window.  |
| plot_pywry_width      | 1400                             | Any positive integer.  | PyWry window width.  |
| plot_pywry_height     | 762                              | Any positive integer.  | PyWry window height. |
| plot_open_export      | False                            | [True, False]        | Controls whether the "Save As" window should pop up as soon as the image is displayed."  |
| table_style           | dark                             | ["dark", "light"]         | "The default color style to use with the OpenBB Charting Extension tables. Options are "dark" and "light""   |
| request_timeout       | 15                               | Any positive integer.  | Specifies the timeout duration for HTTP requests.  |
| metadata              | True                             | [True, False]        | Enables or disables the collection of metadata  which provides information about operations  including arguments  duration  route  and timestamp. Disabling this feature may improve performance in cases where contextual information is not needed or when the additional computation time and storage space are a concern.  |
| output_type           | OBBject                          | ["OBBject", "dataframe", "numpy", "dict", "chart", "polars"] | Specifies the type of data the application will output when a command or endpoint is accessed. Note that choosing data formats only available in Python  such as `dataframe`, `numpy` or `polars` will render the application's API non-functional. |
| show_warnings         | True                             | [True, False]        | Enables or disables the display of warnings.  |

### Notes on Preferences

:::note

- If a `OpenBBUserData` folder in not in the home directory, the application will create one on first run. The user preferences with paths all default to this folder, be it exports, styles or data - this can be changed at any time to suit.
- The `OpenBBUserData` will still be created even if preferences are not pointing to it, this is because the application needs a place to store logs and other artifacts.
- One way to export files or images from the OpenBB Platform is to leverage that functionality from the OpenBB Charting Extension. The `export_directory` preference is the location where the extension will attempt to save CSV and image files.
:::

```json
{
    "preferences": {
        "data_directory": "~/OpenBBUserData",
        "export_directory": "~/OpenBBUserData/exports",
        "cache_directory": "~/OpenBBUserData/cache",
        "user_styles_directory": "~/OpenBBUserData/styles/user",
        "charting_extension": "openbb_charting",
        "chart_style": "dark",
        "plot_enable_pywry": true,
        "plot_pywry_width": 1400,
        "plot_pywry_height": 762,
        "plot_open_export": false,
        "table_style": "dark",
        "request_timeout": 15,
        "metadata": true,
        "output_type": "OBBject"
}
}


## Environment Variables

Environment variables are defined in a `.env` file. If this file does not exist, create it inside the same folder `user_settings.json` is located.

- `OPENBB_DEBUG_MODE`: enables verbosity while running the program
- `OPENBB_DEVELOP_MODE`: points hub service to .co or .dev
- `OPENBB_AUTO_BUILD`: enables automatic SDK package build on import
- `OPENBB_CHARTING_EXTENSION`: specifies which charting extension to use
- `OPENBB_API_AUTH_EXTENSION`: specifies which authentication extension to use
- `OPENBB_API_AUTH`: enables API authentication for command endpoints
- `OPENBB_API_USERNAME`: sets API username
- `OPENBB_API_PASSWORD`: sets API password

Variables can be defined for current session only.

```python
import os
os.environ["OPENBB_DEBUG_MODE"] = "True"
from openbb import obb
```

### Proxy Networks

An environment variable can be set, in the `.env` file, to direct the Requests library to a specific address and port.

```env
HTTP_PROXY="<ADDRESS>" or HTTPS_PROXY="<ADDRESS>”
```

For example:

```env
HTTP_PROXY="http://10.10.10.10:8000"
```