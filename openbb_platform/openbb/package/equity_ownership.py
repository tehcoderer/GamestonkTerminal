### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Optional, Union

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated


class ROUTER_equity_ownership(Container):
    """/equity/ownership
    insider_trading
    institutional
    major_holders
    share_statistics
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def insider_trading(
        self,
        symbol: Annotated[
            str, OpenBBCustomParameter(description="Symbol to get data for.")
        ],
        limit: Annotated[
            int,
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 500,
        provider: Optional[Literal["fmp", "intrinio"]] = None,
        **kwargs
    ) -> OBBject:
        """Insider Trading. Information about insider trading.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        limit : int
            The number of data entries to return.
        provider : Optional[Literal['fmp', 'intrinio']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        transaction_type : Literal[None, 'award', 'conversion', 'return', 'expire_short', 'in_kind', 'gift', 'expire_long', 'discretionary', 'other', 'small', 'exempt', 'otm', 'purchase', 'sale', 'tender', 'will', 'itm', 'trust']
            Type of the transaction. (provider: fmp)
        start_date : Optional[datetime.date]
            Start date of the data, in YYYY-MM-DD format. (provider: intrinio)
        end_date : Optional[datetime.date]
            End date of the data, in YYYY-MM-DD format. (provider: intrinio)
        ownership_type : Optional[Literal['D', 'I']]
            Type of ownership. (provider: intrinio)
        sort_by : Optional[Literal['filing_date', 'updated_on']]
            Field to sort by. (provider: intrinio)

        Returns
        -------
        OBBject
            results : List[InsiderTrading]
                Serializable results.
            provider : Optional[Literal['fmp', 'intrinio']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        InsiderTrading
        --------------
        symbol : str
            Symbol representing the entity requested in the data.
        company_cik : Optional[Union[int, str]]
            CIK number of the company.
        filing_date : Optional[Union[date, datetime]]
            Filing date of the trade.
        transaction_date : Optional[date]
            Date of the transaction.
        owner_cik : Optional[Union[int, str]]
            Reporting individual's CIK.
        owner_name : Optional[str]
            Name of the reporting individual.
        owner_title : Optional[str]
            The title held by the reporting individual.
        transaction_type : Optional[str]
            Type of transaction being reported.
        acquisition_or_disposition : Optional[str]
            Acquisition or disposition of the shares.
        security_type : Optional[str]
            The type of security transacted.
        securities_owned : Optional[float]
            Number of securities owned by the reporting individual.
        securities_transacted : Optional[float]
            Number of securities transacted by the reporting individual.
        transaction_price : Optional[float]
            The price of the transaction.
        filing_url : Optional[str]
            Link to the filing.
        form_type : Optional[str]
            Form type of the insider trading. (provider: fmp)
        company_name : Optional[str]
            Name of the company. (provider: intrinio)
        conversion_exercise_price : Optional[float]
            Conversion/Exercise price of the shares. (provider: intrinio)
        deemed_execution_date : Optional[date]
            Deemed execution date of the trade. (provider: intrinio)
        exercise_date : Optional[date]
            Exercise date of the trade. (provider: intrinio)
        expiration_date : Optional[date]
            Expiration date of the derivative. (provider: intrinio)
        underlying_security_title : Optional[str]
            Name of the underlying non-derivative security related to this derivative transaction. (provider: intrinio)
        underlying_shares : Optional[Union[float, int]]
            Number of underlying shares related to this derivative transaction. (provider: intrinio)
        nature_of_ownership : Optional[str]
            Nature of ownership of the insider trading. (provider: intrinio)
        director : Optional[bool]
            Whether the owner is a director. (provider: intrinio)
        officer : Optional[bool]
            Whether the owner is an officer. (provider: intrinio)
        ten_percent_owner : Optional[bool]
            Whether the owner is a 10% owner. (provider: intrinio)
        other_relation : Optional[bool]
            Whether the owner is having another relation. (provider: intrinio)
        derivative_transaction : Optional[bool]
            Whether the owner is having a derivative transaction. (provider: intrinio)
        report_line_number : Optional[int]
            Report line number of the insider trading. (provider: intrinio)

        Example
        -------
        >>> from openbb import obb
        >>> obb.equity.ownership.insider_trading(symbol="AAPL", limit=500)
        """  # noqa: E501

        return self._run(
            "/equity/ownership/insider_trading",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/equity/ownership/insider_trading",
                        ("fmp", "intrinio"),
                    )
                },
                standard_params={
                    "symbol": symbol,
                    "limit": limit,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def institutional(
        self,
        symbol: Annotated[
            str, OpenBBCustomParameter(description="Symbol to get data for.")
        ],
        provider: Optional[Literal["fmp", "intrinio"]] = None,
        **kwargs
    ) -> OBBject:
        """Institutional Ownership. Institutional ownership data.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        provider : Optional[Literal['fmp', 'intrinio']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        include_current_quarter : Optional[bool]
            Include current quarter data. (provider: fmp)
        date : Optional[datetime.date]
            A specific date to get data for. (provider: fmp)
        limit : Optional[int]
            The number of data entries to return. (provider: intrinio)

        Returns
        -------
        OBBject
            results : List[InstitutionalOwnership]
                Serializable results.
            provider : Optional[Literal['fmp', 'intrinio']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        InstitutionalOwnership
        ----------------------
        symbol : str
            Symbol representing the entity requested in the data.
        cik : Optional[str]
            Central Index Key (CIK) for the requested entity.
        date : date
            The date of the data.
        investors_holding : Optional[int]
            Number of investors holding the stock. (provider: fmp)
        last_investors_holding : Optional[int]
            Number of investors holding the stock in the last quarter. (provider: fmp)
        investors_holding_change : Optional[int]
            Change in the number of investors holding the stock. (provider: fmp)
        number_of_13f_shares : Optional[int]
            Number of 13F shares. (provider: fmp)
        last_number_of_13f_shares : Optional[int]
            Number of 13F shares in the last quarter. (provider: fmp)
        number_of_13f_shares_change : Optional[int]
            Change in the number of 13F shares. (provider: fmp)
        total_invested : Optional[float]
            Total amount invested. (provider: fmp)
        last_total_invested : Optional[float]
            Total amount invested in the last quarter. (provider: fmp)
        total_invested_change : Optional[float]
            Change in the total amount invested. (provider: fmp)
        ownership_percent : Optional[float]
            Ownership percent. (provider: fmp)
        last_ownership_percent : Optional[float]
            Ownership percent in the last quarter. (provider: fmp)
        ownership_percent_change : Optional[float]
            Change in the ownership percent. (provider: fmp)
        new_positions : Optional[int]
            Number of new positions. (provider: fmp)
        last_new_positions : Optional[int]
            Number of new positions in the last quarter. (provider: fmp)
        new_positions_change : Optional[int]
            Change in the number of new positions. (provider: fmp)
        increased_positions : Optional[int]
            Number of increased positions. (provider: fmp)
        last_increased_positions : Optional[int]
            Number of increased positions in the last quarter. (provider: fmp)
        increased_positions_change : Optional[int]
            Change in the number of increased positions. (provider: fmp)
        closed_positions : Optional[int]
            Number of closed positions. (provider: fmp)
        last_closed_positions : Optional[int]
            Number of closed positions in the last quarter. (provider: fmp)
        closed_positions_change : Optional[int]
            Change in the number of closed positions. (provider: fmp)
        reduced_positions : Optional[int]
            Number of reduced positions. (provider: fmp)
        last_reduced_positions : Optional[int]
            Number of reduced positions in the last quarter. (provider: fmp)
        reduced_positions_change : Optional[int]
            Change in the number of reduced positions. (provider: fmp)
        total_calls : Optional[int]
            Total number of call options contracts traded for Apple Inc. on the specified date. (provider: fmp)
        last_total_calls : Optional[int]
            Total number of call options contracts traded for Apple Inc. on the previous reporting date. (provider: fmp)
        total_calls_change : Optional[int]
            Change in the total number of call options contracts traded between the current and previous reporting dates. (provider: fmp)
        total_puts : Optional[int]
            Total number of put options contracts traded for Apple Inc. on the specified date. (provider: fmp)
        last_total_puts : Optional[int]
            Total number of put options contracts traded for Apple Inc. on the previous reporting date. (provider: fmp)
        total_puts_change : Optional[int]
            Change in the total number of put options contracts traded between the current and previous reporting dates. (provider: fmp)
        put_call_ratio : Optional[float]
            Put-call ratio, which is the ratio of the total number of put options to call options traded on the specified date. (provider: fmp)
        last_put_call_ratio : Optional[float]
            Put-call ratio on the previous reporting date. (provider: fmp)
        put_call_ratio_change : Optional[float]
            Change in the put-call ratio between the current and previous reporting dates. (provider: fmp)
        name : Optional[str]
            Name of the institutional owner. (provider: intrinio)
        value : Optional[float]
            Value of the institutional owner. (provider: intrinio)
        amount : Optional[float]
            Amount of the institutional owner. (provider: intrinio)
        sole_voting_authority : Optional[float]
            Sole voting authority of the institutional owner. (provider: intrinio)
        shared_voting_authority : Optional[float]
            Shared voting authority of the institutional owner. (provider: intrinio)
        no_voting_authority : Optional[float]
            No voting authority of the institutional owner. (provider: intrinio)
        previous_amount : Optional[float]
            Previous amount of the institutional owner. (provider: intrinio)
        amount_change : Optional[float]
            Amount change of the institutional owner. (provider: intrinio)
        amount_percent_change : Optional[float]
            Amount percent change of the institutional owner. (provider: intrinio)

        Example
        -------
        >>> from openbb import obb
        >>> obb.equity.ownership.institutional(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/equity/ownership/institutional",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/equity/ownership/institutional",
                        ("fmp", "intrinio"),
                    )
                },
                standard_params={
                    "symbol": symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def major_holders(
        self,
        symbol: Annotated[
            str, OpenBBCustomParameter(description="Symbol to get data for.")
        ],
        date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(description="A specific date to get data for."),
        ] = None,
        page: Annotated[
            Optional[int],
            OpenBBCustomParameter(description="Page number of the data to fetch."),
        ] = 0,
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
        """Equity Ownership. Information about the company ownership.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        date : Union[datetime.date, None, str]
            A specific date to get data for.
        page : Optional[int]
            Page number of the data to fetch.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[EquityOwnership]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EquityOwnership
        ---------------
        date : date
            The date of the data.
        cik : int
            Central Index Key (CIK) for the requested entity.
        filing_date : date
            Filing date of the stock ownership.
        investor_name : str
            Investor name of the stock ownership.
        symbol : str
            Symbol representing the entity requested in the data.
        security_name : str
            Security name of the stock ownership.
        type_of_security : str
            Type of security of the stock ownership.
        security_cusip : str
            Security cusip of the stock ownership.
        shares_type : str
            Shares type of the stock ownership.
        put_call_share : str
            Put call share of the stock ownership.
        investment_discretion : str
            Investment discretion of the stock ownership.
        industry_title : str
            Industry title of the stock ownership.
        weight : float
            Weight of the stock ownership.
        last_weight : float
            Last weight of the stock ownership.
        change_in_weight : float
            Change in weight of the stock ownership.
        change_in_weight_percentage : float
            Change in weight percentage of the stock ownership.
        market_value : int
            Market value of the stock ownership.
        last_market_value : int
            Last market value of the stock ownership.
        change_in_market_value : int
            Change in market value of the stock ownership.
        change_in_market_value_percentage : float
            Change in market value percentage of the stock ownership.
        shares_number : int
            Shares number of the stock ownership.
        last_shares_number : int
            Last shares number of the stock ownership.
        change_in_shares_number : float
            Change in shares number of the stock ownership.
        change_in_shares_number_percentage : float
            Change in shares number percentage of the stock ownership.
        quarter_end_price : float
            Quarter end price of the stock ownership.
        avg_price_paid : float
            Average price paid of the stock ownership.
        is_new : bool
            Is the stock ownership new.
        is_sold_out : bool
            Is the stock ownership sold out.
        ownership : float
            How much is the ownership.
        last_ownership : float
            Last ownership amount.
        change_in_ownership : float
            Change in ownership amount.
        change_in_ownership_percentage : float
            Change in ownership percentage.
        holding_period : int
            Holding period of the stock ownership.
        first_added : date
            First added date of the stock ownership.
        performance : float
            Performance of the stock ownership.
        performance_percentage : float
            Performance percentage of the stock ownership.
        last_performance : float
            Last performance of the stock ownership.
        change_in_performance : float
            Change in performance of the stock ownership.
        is_counted_for_performance : bool
            Is the stock ownership counted for performance.

        Example
        -------
        >>> from openbb import obb
        >>> obb.equity.ownership.major_holders(symbol="AAPL", page=0)
        """  # noqa: E501

        return self._run(
            "/equity/ownership/major_holders",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/equity/ownership/major_holders",
                        ("fmp",),
                    )
                },
                standard_params={
                    "symbol": symbol,
                    "date": date,
                    "page": page,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def share_statistics(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(
                description="Symbol to get data for. Multiple items allowed: yfinance."
            ),
        ],
        provider: Optional[Literal["fmp", "intrinio", "yfinance"]] = None,
        **kwargs
    ) -> OBBject:
        """Share Statistics. Share statistics for a given company.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for. Multiple items allowed: yfinance.
        provider : Optional[Literal['fmp', 'intrinio', 'yfinance']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[ShareStatistics]
                Serializable results.
            provider : Optional[Literal['fmp', 'intrinio', 'yfinance']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        ShareStatistics
        ---------------
        symbol : str
            Symbol representing the entity requested in the data.
        date : Optional[date]
            The date of the data.
        free_float : Optional[float]
            Percentage of unrestricted shares of a publicly-traded company.
        float_shares : Optional[float]
            Number of shares available for trading by the general public.
        outstanding_shares : Optional[float]
            Total number of shares of a publicly-traded company.
        source : Optional[str]
            Source of the received data.
        adjusted_outstanding_shares : Optional[float]
            Total number of shares of a publicly-traded company, adjusted for splits. (provider: intrinio)
        public_float : Optional[float]
            Aggregate market value of the shares of a publicly-traded company. (provider: intrinio)
        implied_shares_outstanding : Optional[int]
            Implied Shares Outstanding of common equity, assuming the conversion of all convertible subsidiary equity into common. (provider: yfinance)
        short_interest : Optional[int]
            Number of shares that are reported short. (provider: yfinance)
        short_percent_of_float : Optional[float]
            Percentage of shares that are reported short, as a normalized percent. (provider: yfinance)
        days_to_cover : Optional[float]
            Number of days to repurchase the shares as a ratio of average daily volume (provider: yfinance)
        short_interest_prev_month : Optional[int]
            Number of shares that were reported short in the previous month. (provider: yfinance)
        short_interest_prev_date : Optional[date]
            Date of the previous month's report. (provider: yfinance)
        insider_ownership : Optional[float]
            Percentage of shares held by insiders, as a normalized percent. (provider: yfinance)
        institution_ownership : Optional[float]
            Percentage of shares held by institutions, as a normalized percent. (provider: yfinance)
        institution_float_ownership : Optional[float]
            Percentage of float held by institutions, as a normalized percent. (provider: yfinance)
        institutions_count : Optional[int]
            Number of institutions holding shares. (provider: yfinance)

        Example
        -------
        >>> from openbb import obb
        >>> obb.equity.ownership.share_statistics(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/equity/ownership/share_statistics",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/equity/ownership/share_statistics",
                        ("fmp", "intrinio", "yfinance"),
                    )
                },
                standard_params={
                    "symbol": symbol,
                },
                extra_params=kwargs,
                extra_info={"symbol": {"multiple_items_allowed": ["yfinance"]}},
            )
        )
