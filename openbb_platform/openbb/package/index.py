### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Optional, Union
from warnings import simplefilter, warn

from openbb_core.app.deprecation import OpenBBDeprecationWarning
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated, deprecated


class ROUTER_index(Container):
    """/index
    available
    constituents
    market
    /price
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def available(
        self, provider: Optional[Literal["fmp", "yfinance"]] = None, **kwargs
    ) -> OBBject:
        """Available Indices. Available indices for a given provider.

        Parameters
        ----------
        provider : Optional[Literal['fmp', 'yfinance']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[FMPAvailableIndices], Tag(tag='fmp')], Annotated[List[YFinanceAvailableIndices], Tag(tag='yfinance')]]
                Serializable results.
            provider : Optional[Literal['fmp', 'yfinance']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        AvailableIndices
        ----------------
        name : Optional[str]
            Name of the index.
        currency : Optional[str]
            Currency the index is traded in.
        stock_exchange : Optional[str]
            Stock exchange where the index is listed. (provider: fmp)
        exchange_short_name : Optional[str]
            Short name of the stock exchange where the index is listed. (provider: fmp)
        code : Optional[str]
            ID code for keying the index in the OpenBB Terminal. (provider: yfinance)
        symbol : Optional[str]
            Symbol for the index. (provider: yfinance)

        Example
        -------
        >>> from openbb import obb
        >>> obb.index.available()
        """  # noqa: E501

        return self._run(
            "/index/available",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={},
                extra_params=kwargs,
            )
        )

    @validate
    def constituents(
        self,
        index: Annotated[
            str,
            OpenBBCustomParameter(description="Index to fetch the constituents of."),
        ],
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
        """Index Constituents. Constituents of an index.

        Parameters
        ----------
        index : str
            Index to fetch the constituents of.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[FMPIndexConstituents], Tag(tag='fmp')]]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        IndexConstituents
        -----------------
        symbol : str
            Symbol representing the entity requested in the data.
        name : Optional[str]
            Name of the constituent company in the index.
        sector : Optional[str]
            Sector the constituent company in the index belongs to. (provider: fmp)
        sub_sector : Optional[str]
            Sub-sector the constituent company in the index belongs to. (provider: fmp)
        headquarter : Optional[str]
            Location of the headquarter of the constituent company in the index. (provider: fmp)
        date_first_added : Optional[Union[str, date]]
            Date the constituent company was added to the index. (provider: fmp)
        cik : Optional[int]
            Central Index Key (CIK) for the requested entity. (provider: fmp)
        founded : Optional[Union[str, date]]
            Founding year of the constituent company in the index. (provider: fmp)

        Example
        -------
        >>> from openbb import obb
        >>> obb.index.constituents(index="^IBEX")
        """  # noqa: E501

        return self._run(
            "/index/constituents",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "index": index,
                },
                extra_params=kwargs,
            )
        )

    @validate
    @deprecated(
        "This endpoint is deprecated; use `/index/price/historical` instead. Deprecated in OpenBB Platform V4.1 to be removed in V4.3.",
        category=OpenBBDeprecationWarning,
    )
    def market(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        provider: Optional[Literal["fmp", "intrinio", "polygon", "yfinance"]] = None,
        **kwargs
    ) -> OBBject:
        """Historical Market Indices.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        start_date : Optional[datetime.date]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Optional[datetime.date]
            End date of the data, in YYYY-MM-DD format.
        provider : Optional[Literal['fmp', 'intrinio', 'polygon', 'yfinance']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        timeseries : Optional[Annotated[int, Ge(ge=0)]]
            Number of days to look back. (provider: fmp)
        interval : Optional[Union[Literal['1min', '5min', '15min', '30min', '1hour', '4hour', '1day'], Literal['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']]]
            Data granularity. (provider: fmp, yfinance)
        sort : Literal['asc', 'desc']
            Sort the data in ascending or descending order. (provider: fmp);
            Sort order. (provider: intrinio);
            Sort order of the data. (provider: polygon)
        tag : Optional[str]
            Index tag. (provider: intrinio)
        type : Optional[str]
            Index type. (provider: intrinio)
        limit : int
            The number of data entries to return. (provider: intrinio, polygon)
        timespan : Literal['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']
            Timespan of the data. (provider: polygon)
        adjusted : bool
            Whether the data is adjusted. (provider: polygon)
        multiplier : int
            Multiplier of the timespan. (provider: polygon)
        period : Optional[Literal['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']]
            Time period of the data to return. (provider: yfinance)
        prepost : bool
            Include Pre and Post market data. (provider: yfinance)
        rounding : bool
            Round prices to two decimals? (provider: yfinance)

        Returns
        -------
        OBBject
            results : Union[Annotated[Union[list, dict], Tag(tag='openbb')], Annotated[List[FMPMarketIndices], Tag(tag='fmp')], Annotated[List[IntrinioMarketIndices], Tag(tag='intrinio')], Annotated[List[PolygonMarketIndices], Tag(tag='polygon')], Annotated[List[YFinanceMarketIndices], Tag(tag='yfinance')]]
                Serializable results.
            provider : Optional[Literal['fmp', 'intrinio', 'polygon', 'yfinance']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        MarketIndices
        -------------
        date : datetime
            The date of the data.
        open : Optional[Annotated[float, Strict(strict=True)]]
            The open price.
        high : Optional[Annotated[float, Strict(strict=True)]]
            The high price.
        low : Optional[Annotated[float, Strict(strict=True)]]
            The low price.
        close : Optional[Annotated[float, Strict(strict=True)]]
            The close price.
        volume : Optional[int]
            The trading volume.
        adj_close : Optional[float]
            The adjusted close price. (provider: fmp)
        unadjusted_volume : Optional[float]
            Unadjusted volume of the symbol. (provider: fmp)
        change : Optional[float]
            Change in the price of the symbol from the previous day. (provider: fmp)
        change_percent : Optional[float]
            Change % in the price of the symbol. (provider: fmp)
        label : Optional[str]
            Human readable format of the date. (provider: fmp)
        change_over_time : Optional[float]
            Change % in the price of the symbol over a period of time. (provider: fmp)
        transactions : Optional[Annotated[int, Gt(gt=0)]]
            Number of transactions for the symbol in the time period. (provider: polygon)

        Example
        -------
        >>> from openbb import obb
        >>> obb.index.market(symbol="SPX")
        """  # noqa: E501

        simplefilter("always", DeprecationWarning)
        warn(
            "This endpoint is deprecated; use `/index/price/historical` instead. Deprecated in OpenBB Platform V4.1 to be removed in V4.3.",
            category=DeprecationWarning,
            stacklevel=2,
        )

        return self._run(
            "/index/market",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                extra_params=kwargs,
            )
        )

    @property
    def price(self):
        # pylint: disable=import-outside-toplevel
        from . import index_price

        return index_price.ROUTER_index_price(command_runner=self._command_runner)
