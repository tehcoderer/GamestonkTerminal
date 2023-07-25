"""ProviderRegistry class and Builder class."""


from typing import Any, Dict, Optional

import pkg_resources

from openbb_provider.abstract.data import QueryParams
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.abstract.provider import Provider


class ProviderError(Exception):
    pass


# TODO: This ProviderRegistry needs some refactoring. The two attributes partially
# repeat themselves.


class ProviderRegistry:
    """A Provider Registry a class that holds all the providers and their credentials."""

    def __init__(
        self, providers: Dict[str, Provider], credentials: Dict[str, Dict[str, None]]
    ) -> None:
        self.providers: Dict[str, Provider] = providers
        self.credentials: Dict[str, Dict[str, None]] = credentials

    def get_provider(self, provider_name: str) -> Provider:
        """Get a provider from the registry."""
        if not self.providers:
            raise ValueError("No providers found, please confirm they are loaded.")

        try:
            provider = self.providers[provider_name]
        except KeyError as e:
            raise ValueError(
                f"{provider_name} is not part of the ProviderRegistry. "
                f"Available providers are: {list(self.providers.keys())}"
            ) from e

        return provider

    def filter_credentials(
        self,
        provider_name: str,
        credentials: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        required_credentials = self.credentials.get(provider_name)

        if required_credentials is None:
            return {}

        result: Dict[str, str] = {}
        if credentials is not None:
            for k in required_credentials:
                credential_value = credentials.get(k)
                if k not in credentials or credential_value is None:
                    raise ProviderError(
                        f"Missing credential '{k}' for '{provider_name}'."
                    )

                result[k] = credential_value

        return result

    def get_fetcher(self, provider: Provider, query_params: QueryParams) -> Fetcher:
        """Get a fetcher from the provider."""
        fetch_dict = provider.fetcher_dict[
            "get_query_type"
        ]  # TODO: Check if we really need to pass this "get_query_type"
        fetcher = fetch_dict.get(query_params.__name__)  # type: ignore
        if fetcher is None:
            raise ProviderError(
                f"This query is not supported by the '{provider.name}' provider. "
                f"Please try another provider: '{list(self.providers.keys())}'"
            )
        return fetcher

    def fetch(
        self,
        provider_name: str,
        query_params: QueryParams,
        extra_params: Optional[Dict] = None,
        credentials: Optional[Dict[str, str]] = None,
    ):
        """Fetch data from a provider by using the OpenBB standard."""
        provider = self.get_provider(provider_name)
        filtered_credentials = self.filter_credentials(provider_name, credentials)
        Fetcher_ = self.get_fetcher(provider, query_params)

        try:
            return Fetcher_.fetch_data(query_params, extra_params, filtered_credentials)
        except Exception as e:
            raise ProviderError(e) from e


def load_extensions(
    entry_point_group: str = "openbb_provider_extension",
) -> Dict[str, Dict[str, Any]]:
    """Load extensions from entry points and their API keys from settings."""

    # TODO: This function is overcomplicated and needs refactoring.

    extensions_dict: Dict[str, Dict[str, Any]] = {}
    extensions_dict["providers"] = {}
    extensions_dict["credentials"] = {}

    entry_points = pkg_resources.iter_entry_points(entry_point_group)
    for entry_point in entry_points:
        e = entry_point.load()

        provider_name = str(e.name)

        extensions_dict["providers"][provider_name] = e

        required_credentials = getattr(e, "required_credentials", None)
        if required_credentials:
            extensions_dict["credentials"][provider_name] = {}
            for credential in required_credentials:
                if credential:
                    credential_name = provider_name.lower() + "_" + credential.lower()
                    extensions_dict["credentials"][provider_name][
                        credential_name
                    ] = None

    return extensions_dict


def build_provider_registry(
    extensions_dict: Dict[str, Dict[str, Any]]
) -> ProviderRegistry:
    """Build a ProviderRegistry from a list of extensions and their API keys."""
    return ProviderRegistry(
        extensions_dict["providers"], extensions_dict["credentials"]
    )


extensions_dict__ = load_extensions("openbb_provider_extension")
provider_registry = build_provider_registry(extensions_dict=extensions_dict__)