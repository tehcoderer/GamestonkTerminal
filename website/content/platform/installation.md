---
title: Installation
sidebar_position: 1
description: This page presents the general system requirements, supported environments,
  installation procedures, and setup for running the OpenBB Platform. It discusses
  the prerequisites including Python version, operating system requirements, Docker
  usage, and the process of building the platform from source.
keywords:
- OpenBB Platform
- Python
- System requirements
- Supported environments
- Installation
- Docker
- Python virtual environment
- Installation from source
- Windows 10
- Mac OS Big Sur
- Linux
- Package installation
- VS Code
- PyCharm
- Jupyter
- GitHub
- Conda
- venv
- API
- Repository
- pip
- Poetry
- Toml
- PyPI
- Node.js
- npm
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Installation | OpenBB Platform Docs" />

## General System Requirements

Most systems capable of running Python 3.8-3.11 will be compatible with the OpenBB Platform.  A modern processor (five years or less), running an up-to-date operating system, with at least 4GB of RAM, is recommended.  Maintaining the system with current patches ensures maximum compatibility.  At a minimum, Windows and macOS should be:

- Windows 10
- Mac OS Big Sur

Linux users should run the command line update for the package manager, prior to installation.

## Supported Environments

The OpenBB Platform is installed within a Python virtual environment.  It is compatible with versions of Python between 3.8 and 3.11, inclusively.  The method for creating the environment will be a matter of user preference, from the command line - [Conda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html), [venv](https://docs.python.org/3/library/venv.html),  [Docker](https://hub.docker.com/), etc. - or in a code editor and IDE - [VS Code](https://code.visualstudio.com/docs/languages/python), [PyCharm](https://www.jetbrains.com/pycharm/), [Jupyter](https://jupyter.org/).

[Docker](/platform/installation#docker) builds the environment during the installation process, skip ahead to the specific section [below](/platform/installation#docker).

For those new to Python, [this article](https://www.infoworld.com/article/3306656/python-virtualenv-and-venv-dos-and-donts.html) shares some tips on getting started and why environments are important.

See [this guide](https://code.visualstudio.com/docs/python/environments) for creating a Python environment in VS Code.

With the container created, and activated, begin the installation process.

## Installation

Before installation, update the package manager so that `pip` is current, then create the environment with the desired version of Python and install the following packages:

:::note
Installing packages directly to the system Python or `base` environment is not recommended.  Create a new environment.
:::

```console
pip install poetry toml
```

### PyPI

Install from PyPI with:

```console
pip install openbb --pre
```

To install all of the extensions and providers:

```console
pip install openbb[all] --pre
```

:::note
While still under active development, the `pre` flag is required to install the core OpenBB Platform latest version.
:::

To install a single extension:

```console
pip install openbb[charting] --pre
```

```console
pip install openbb[ta] --pre
```

Import the package with:

```console
from openbb import obb
```

### Docker

OpenBB supplies a `.dockerfile` on [GitHub](https://github.com/OpenBB-finance/OpenBBTerminal).

Run the following command from the repo root to build the image:

```bash
docker build -f build/docker/api.dockerfile -t openbb-platform:latest .
```

To run it:

```bash
docker run --rm -p 8000:8000 -v ~/.openbb_platform:/root/.openbb_platform openbb-platform:latest
```

This will mount the local `~/.openbb_platform` directory into the Docker container to use with the API keys and preferences from there, and it will expose the API on port `8000`.

### Source

To build the OpenBB Platform from the source code, first install `git`:

```console
pip install git
```

Next, clone the repository from GitHub:

```console
git clone git@github.com:OpenBB-finance/OpenBBTerminal.git
```

When it is done, checkout the branch where the code is living:

```console
git checkout feature/openbb-sdk-v4
```

Then, `cd` into the directory:

```console
cd openbb_platform
```

Finally, run the developer installation script:

```console
python dev_install.py
```

:::note
To install all extensions and providers, run: `python dev_install.py -e`
:::

With a fresh installation, or upon installing or uninstalling extensions, the Python interface needs to be built.  This is done automatically, but can be manually triggered if required.  Start a Python session and then `import openbb`:

```console
python

import openbb

exit()
```

To manually trigger the build:

```python
import openbb
openbb.build()
```

Restart the Python interpreter and then begin using the OpenBB Platform.

```python
from openbb import obb
```

Start the REST API with:

```console
uvicorn openbb_core.api.rest_api:app --host 0.0.0.0 --port 8000 --reload
```

## Documentation

The documentation and packages are kept in the `/website` folder, at the base of the repository.  Navigate there to install the dependencies and start the development server.

#### Node.js

- [Node.js](https://nodejs.org/en/) >= 16.13.0
  To check if Node.js installed, run this command:

```bash
node --version # should be v16.13.0 or higher
```

#### Install Dependencies

```bash
npm install
```

#### Start Development Server

```bash
npm start
```

This starts a local development server at: [http://localhost:3000](http://localhost:3000)

Most changes are reflected live without having to restart the server.

#### Build

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service. OpenBB uses Github Pages to host our website, it's deployed in the `gh-pages` branch.
