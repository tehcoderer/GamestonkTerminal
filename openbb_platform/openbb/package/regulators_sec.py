### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import List, Literal, Optional, Union

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated


class ROUTER_regulators_sec(Container):
    """/regulators/sec
    cik_map
    institutions_search
    rss_litigation
    schema_files
    sic_search
    symbol_map
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def cik_map(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        provider: Optional[Literal["sec"]] = None,
        **kwargs
    ) -> OBBject:
        """Get the CIK number corresponding to a ticker symbol.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[SecCikMap, Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        CikMap
        ------
        cik : Optional[Union[str, int]]
            Central Index Key (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.cik_map(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/regulators/sec/cik_map",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def institutions_search(
        self,
        query: Annotated[str, OpenBBCustomParameter(description="Search query.")] = "",
        use_cache: Annotated[
            Optional[bool],
            OpenBBCustomParameter(
                description="Whether or not to use cache. If True, cache will store for seven days."
            ),
        ] = True,
        provider: Optional[Literal["sec"]] = None,
        **kwargs
    ) -> OBBject:
        """Look up institutions regulated by the SEC.

        Parameters
        ----------
        query : str
            Search query.
        use_cache : Optional[bool]
            Whether or not to use cache. If True, cache will store for seven days.
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[SecInstitutionsSearch], Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        InstitutionsSearch
        ------------------
        name : Optional[str]
            The name of the institution. (provider: sec)
        cik : Optional[Union[str, int]]
            Central Index Key (CIK) (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.institutions_search(query="AAPL", use_cache=True)
        """  # noqa: E501

        return self._run(
            "/regulators/sec/institutions_search",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                    "use_cache": use_cache,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def rss_litigation(
        self, provider: Optional[Literal["sec"]] = None, **kwargs
    ) -> OBBject:
        """The RSS feed provides links to litigation releases concerning civil lawsuits brought by the Commission in federal court.

        Parameters
        ----------
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[SecRssLitigation], Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        RssLitigation
        -------------
        published : Optional[datetime]
            The date of publication. (provider: sec)
        title : Optional[str]
            The title of the release. (provider: sec)
        summary : Optional[str]
            Short summary of the release. (provider: sec)
        id : Optional[str]
            The identifier associated with the release. (provider: sec)
        link : Optional[str]
            URL to the release. (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.rss_litigation()
        """  # noqa: E501

        return self._run(
            "/regulators/sec/rss_litigation",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={},
                extra_params=kwargs,
            )
        )

    @validate
    def schema_files(
        self,
        query: Annotated[str, OpenBBCustomParameter(description="Search query.")] = "",
        use_cache: Annotated[
            Optional[bool],
            OpenBBCustomParameter(
                description="Whether or not to use cache. If True, cache will store for seven days."
            ),
        ] = True,
        provider: Optional[Literal["sec"]] = None,
        **kwargs
    ) -> OBBject:
        """Get lists of SEC XML schema files by year.

        Parameters
        ----------
        query : str
            Search query.
        use_cache : Optional[bool]
            Whether or not to use cache. If True, cache will store for seven days.
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.
        url : Optional[str]
            Enter an optional URL path to fetch the next level. (provider: sec)

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[SecSchemaFiles, Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        SchemaFiles
        -----------
        files : Optional[List]
            Dictionary of URLs to SEC Schema Files (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.schema_files(query="AAPL", use_cache=True)
        """  # noqa: E501

        return self._run(
            "/regulators/sec/schema_files",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                    "use_cache": use_cache,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def sic_search(
        self,
        query: Annotated[str, OpenBBCustomParameter(description="Search query.")] = "",
        use_cache: Annotated[
            Optional[bool],
            OpenBBCustomParameter(
                description="Whether or not to use cache. If True, cache will store for seven days."
            ),
        ] = True,
        provider: Optional[Literal["sec"]] = None,
        **kwargs
    ) -> OBBject:
        """Search for Industry Titles, Reporting Office, and SIC Codes.

        Parameters
        ----------
        query : str
            Search query.
        use_cache : Optional[bool]
            Whether or not to use cache. If True, cache will store for seven days.
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[SecSicSearch], Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        SicSearch
        ---------
        sic : Optional[int]
            Sector Industrial Code (SIC) (provider: sec)
        industry : Optional[str]
            Industry title. (provider: sec)
        office : Optional[str]
            Reporting office within the Corporate Finance Office (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.sic_search(query="AAPL", use_cache=True)
        """  # noqa: E501

        return self._run(
            "/regulators/sec/sic_search",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                    "use_cache": use_cache,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def symbol_map(
        self,
        query: Annotated[str, OpenBBCustomParameter(description="Search query.")] = "",
        use_cache: Annotated[
            Optional[bool],
            OpenBBCustomParameter(
                description="Whether or not to use cache. If True, cache will store for seven days."
            ),
        ] = True,
        provider: Optional[Literal["sec"]] = None,
        **kwargs
    ) -> OBBject:
        """Get the ticker symbol corresponding to a company's CIK.

        Parameters
        ----------
        query : str
            Search query.
        use_cache : Optional[bool]
            Whether or not to use cache. If True, cache will store for seven days.
        provider : Optional[Literal['sec']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'sec' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[SecSymbolMap, Tag(tag='sec')]]
                Serializable results.
            provider : Optional[Literal['sec']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        SymbolMap
        ---------
        symbol : Optional[str]
            Symbol representing the entity requested in the data. (provider: sec)

        Example
        -------
        >>> from openbb import obb
        >>> obb.regulators.sec.symbol_map(query="AAPL", use_cache=True)
        """  # noqa: E501

        return self._run(
            "/regulators/sec/symbol_map",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                    "use_cache": use_cache,
                },
                extra_params=kwargs,
            )
        )
