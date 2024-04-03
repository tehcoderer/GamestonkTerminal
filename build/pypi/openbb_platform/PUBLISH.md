# Publishing to PyPI

## Pre-release procedure

> [!WARNING]
> The `release` branch is solely for the purpose of publishing the package(s)! Any last minute changes should be made in appropriate PRs and merged to the `develop` branch. Once the `release` branch is created, the `develop` branch should be frozen for further commits.

> A `release` branch for a particular package should only cater to the changes for that package directory. For e.g. the `release/openbb-core-2.0.0` branch should only contain changes for the `openbb-core` package i.e. in the `openbb_platform/core` directory.

1. Open a PR with the changes to be published in the format `release/<version>` (for e.g. `release/4.0.0` ). For a particular package use the format `release/<package>-<version>` (for e.g. `release/openbb-core-1.0.1`).
2. Ensure all the CI workflows pass.
3. Ensure all unit tests pass: `pytest openbb_platform -m "not integration"`
4. Ensure all integration tests pass: `pytest openbb_platform -m integration`
5. Run `python -c "import openbb; openbb.build()"` to build the static assets. Make sure that only required extensions are installed.

    > **Note**: Run `python -c "import openbb"` after building the static to check that no additional static is being built.

6. Finally, check if everything works:

   1. Install the packages locally using `python openbb_platform/dev_install.py` command and test them in a new environment.
   2. Check if all the `pyproject.toml` files are correct, including the `openbb_platform` one.
   3. Double check if there is any new extension or provider that needs to be added to [integration tests GitHub Action workflow](/.github/workflows/platform-api-integration-test.yml).

## Release procedure

> Ensure you have the appropriate credentials and permissions to publish to PyPI.

1. Run the following commands for publishing the packages to PyPI:

    Consider using the `--dry-run` flag to check if everything is correct before publishing.
    Also, it might be a good idea to run the script in batches to ensure that the packages are published correctly and the dependencies pick the correct versions.

    > For a single package release, the following steps are optional since the package can be bumped manually.

    1. For the core package run: `python build/pypi/openbb_platform/publish.py --core`
    2. For the extension and provider packages run: `python build/pypi/openbb_platform/publish.py --extensions`
    3. For the `openbb` package - **which requires manual publishing** - do the following
         - Bump the dependency package versions
         - Re-build the static assets that are bundled with the package
         - Run unit tests to validate the existence of deprecated endpoints
         - Run `poetry publish --build` from `openbb_platform`
         - Run `poetry lock` from `openbb_platform`

    > [!TIP]
    > Note that, in order for packages to pick up the latest versions of dependencies, it is advised to clear the local cache of the dependencies:
    >
    > We can do that with `pip cache purge` and `poetry cache clear pypi --all`
    >
    > Also, sometimes there might be some delay in the PyPI API, so it might be necessary to wait a few minutes before publishing the next package.

2. Merge the `release/<package>-<version>` branch to the `main` branch.
3. Check the `Deploy to GitHub Pages` GitHub action is completed successfully. Go to the [docs](https://docs.openbb.co) website to see the changes.

## Post-release procedure

1. Install the packages on Google Colaboratory via PyPi and test to check if everything is working as expected.
2. Install the packages in a new environment locally via PyPi and test to check if everything is working as expected.
3. Open a new PR with the `release/<package>-<version>` branch pointing to the `develop` branch.
4. Merge the `release/<package>-<version>` branch to the `develop` branch.
5. If any bugs are encountered, create a new branch - `hotfix` for `main` and `bugfix` for `develop` and merge them accordingly.
