### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Union

import typing_extensions
from annotated_types import Ge
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.filters import filter_inputs
from openbb_provider.abstract.data import Data
from pydantic import validate_call


class ROUTER_stocks(Container):
    """/stocks
    /ca
    /fa
    load
    multiples
    news
    /options
    quote
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def ca(self):  # route = "/stocks/ca"
        from . import stocks_ca

        return stocks_ca.ROUTER_stocks_ca(command_runner=self._command_runner)

    @property
    def fa(self):  # route = "/stocks/fa"
        from . import stocks_fa

        return stocks_fa.ROUTER_stocks_fa(command_runner=self._command_runner)

    @validate_call
    def load(
        self,
        symbol: typing_extensions.Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        start_date: typing_extensions.Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: typing_extensions.Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        provider: Union[Literal["fmp", "intrinio", "polygon"], None] = None,
        **kwargs
    ) -> OBBject[List[Data]]:
        """Load stock data for a specific ticker.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        start_date : Union[datetime.date, None]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, None]
            End date of the data, in YYYY-MM-DD format.
        provider : Union[Literal['fmp', 'intrinio', 'polygon'], None]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        timeseries : Optional[Union[typing_extensions.Annotated[int, Ge(ge=0)]]]
            Number of days to look back. (provider: fmp)
        interval : Literal['1min', '5min', '15min', '30min', '1hour', '4hour', '1day']
            Data granularity. (provider: fmp)
        timezone : Optional[Union[Literal['Africa/Algiers', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Monrovia', 'Africa/Nairobi', 'America/Argentina/Buenos_Aires', 'America/Bogota', 'America/Caracas', 'America/Chicago', 'America/Chihuahua', 'America/Denver', 'America/Godthab', 'America/Guatemala', 'America/Guyana', 'America/Halifax', 'America/Indiana/Indianapolis', 'America/Juneau', 'America/La_Paz', 'America/Lima', 'America/Lima', 'America/Los_Angeles', 'America/Mazatlan', 'America/Mexico_City', 'America/Mexico_City', 'America/Monterrey', 'America/Montevideo', 'America/New_York', 'America/Phoenix', 'America/Regina', 'America/Santiago', 'America/Sao_Paulo', 'America/St_Johns', 'America/Tijuana', 'Asia/Almaty', 'Asia/Baghdad', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Bangkok', 'Asia/Chongqing', 'Asia/Colombo', 'Asia/Dhaka', 'Asia/Dhaka', 'Asia/Hong_Kong', 'Asia/Irkutsk', 'Asia/Jakarta', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Karachi', 'Asia/Kathmandu', 'Asia/Kolkata', 'Asia/Kolkata', 'Asia/Kolkata', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuwait', 'Asia/Magadan', 'Asia/Muscat', 'Asia/Muscat', 'Asia/Novosibirsk', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tokyo', 'Asia/Tokyo', 'Asia/Tokyo', 'Asia/Ulaanbaatar', 'Asia/Urumqi', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Cape_Verde', 'Atlantic/South_Georgia', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Darwin', 'Australia/Hobart', 'Australia/Melbourne', 'Australia/Melbourne', 'Australia/Perth', 'Australia/Sydney', 'Etc/UTC', 'UTC', 'Europe/Amsterdam', 'Europe/Athens', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Helsinki', 'Europe/Istanbul', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/London', 'Europe/Madrid', 'Europe/Minsk', 'Europe/Moscow', 'Europe/Moscow', 'Europe/Paris', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/Sarajevo', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Auckland', 'Pacific/Chatham', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Majuro', 'Pacific/Midway', 'Pacific/Midway', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Port_Moresby', 'Pacific/Tongatapu']]]
            Returns trading times in this timezone. (provider: intrinio)
        source : Optional[Union[Literal['realtime', 'delayed', 'nasdaq_basic']]]
            The source of the data. (provider: intrinio)
        start_time : Optional[Union[datetime.time]]
            Return intervals starting at the specified time on the `start_date` formatted as 'hh:mm:ss'. (provider: intrinio)
        end_time : Optional[Union[datetime.time]]
            Return intervals stopping at the specified time on the `end_date` formatted as 'hh:mm:ss'. (provider: intrinio)
        interval_size : Optional[Union[Literal['1m', '5m', '10m', '15m', '30m', '60m', '1h']]]
            The data time frequency. (provider: intrinio)
        multiplier : int
            Multiplier of the timespan. (provider: polygon)
        timespan : Literal['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']
            Timespan of the data. (provider: polygon)
        sort : Literal['asc', 'desc']
            Sort order of the data. (provider: polygon)
        limit : int
            The number of data entries to return. (provider: polygon)
        adjusted : bool
            Output time series is adjusted by historical split and dividend events. (provider: polygon)

        Returns
        -------
        OBBject
            results : Union[List[StockHistorical]]
                Serializable results.
            provider : Union[Literal['fmp', 'intrinio', 'polygon'], None]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        StockHistorical
        ---------------
        date : datetime
            The date of the data.
        open : float
            The open price of the symbol.
        high : float
            The high price of the symbol.
        low : float
            The low price of the symbol.
        close : float
            The close price of the symbol.
        volume : Union[float, int]
            The volume of the symbol.
        vwap : Optional[Union[typing_extensions.Annotated[float, Gt(gt=0)]]]
            Volume Weighted Average Price of the symbol.
        adj_close : Optional[Union[float]]
            Adjusted Close Price of the symbol. (provider: fmp)
        unadjusted_volume : Optional[Union[float]]
            Unadjusted volume of the symbol. (provider: fmp)
        change : Optional[Union[float]]
            Change in the price of the symbol from the previous day. (provider: fmp, intrinio)
        change_percent : Optional[Union[float]]
            Change % in the price of the symbol. (provider: fmp)
        label : Optional[Union[str]]
            Human readable format of the date. (provider: fmp)
        change_over_time : Optional[Union[float]]
            Change % in the price of the symbol over a period of time. (provider: fmp)
        close_time : Optional[Union[datetime]]
            The timestamp that represents the end of the interval span. (provider: intrinio)
        interval : Optional[Union[str]]
            The data time frequency. (provider: intrinio)
        average : Optional[Union[float]]
            Average trade price of an individual stock during the interval. (provider: intrinio)
        transactions : Optional[Union[typing_extensions.Annotated[int, Gt(gt=0)]]]
            Number of transactions for the symbol in the time period. (provider: polygon)
        """  # noqa: E501

        inputs = filter_inputs(
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

        return self._run(
            "/stocks/load",
            **inputs,
        )

    @validate_call
    def multiples(
        self,
        symbol: typing_extensions.Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        limit: typing_extensions.Annotated[
            Union[int, None],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 100,
        provider: Union[Literal["fmp"], None] = None,
        **kwargs
    ) -> OBBject[List[Data]]:
        """Get valuation multiples for a stock ticker.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        limit : Union[int, None]
            The number of data entries to return.
        provider : Union[Literal['fmp'], None]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : Union[List[StockMultiples]]
                Serializable results.
            provider : Union[Literal['fmp'], None]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        StockMultiples
        --------------
        revenue_per_share_ttm : Optional[Union[float]]
            Revenue per share calculated as trailing twelve months.
        net_income_per_share_ttm : Optional[Union[float]]
            Net income per share calculated as trailing twelve months.
        operating_cash_flow_per_share_ttm : Optional[Union[float]]
            Operating cash flow per share calculated as trailing twelve months.
        free_cash_flow_per_share_ttm : Optional[Union[float]]
            Free cash flow per share calculated as trailing twelve months.
        cash_per_share_ttm : Optional[Union[float]]
            Cash per share calculated as trailing twelve months.
        book_value_per_share_ttm : Optional[Union[float]]
            Book value per share calculated as trailing twelve months.
        tangible_book_value_per_share_ttm : Optional[Union[float]]
            Tangible book value per share calculated as trailing twelve months.
        shareholders_equity_per_share_ttm : Optional[Union[float]]
            Shareholders equity per share calculated as trailing twelve months.
        interest_debt_per_share_ttm : Optional[Union[float]]
            Interest debt per share calculated as trailing twelve months.
        market_cap_ttm : Optional[Union[float]]
            Market capitalization calculated as trailing twelve months.
        enterprise_value_ttm : Optional[Union[float]]
            Enterprise value calculated as trailing twelve months.
        pe_ratio_ttm : Optional[Union[float]]
            Price-to-earnings ratio (P/E ratio) calculated as trailing twelve months.
        price_to_sales_ratio_ttm : Optional[Union[float]]
            Price-to-sales ratio calculated as trailing twelve months.
        pocf_ratio_ttm : Optional[Union[float]]
            Price-to-operating cash flow ratio calculated as trailing twelve months.
        pfcf_ratio_ttm : Optional[Union[float]]
            Price-to-free cash flow ratio calculated as trailing twelve months.
        pb_ratio_ttm : Optional[Union[float]]
            Price-to-book ratio calculated as trailing twelve months.
        ptb_ratio_ttm : Optional[Union[float]]
            Price-to-tangible book ratio calculated as trailing twelve months.
        ev_to_sales_ttm : Optional[Union[float]]
            Enterprise value-to-sales ratio calculated as trailing twelve months.
        enterprise_value_over_ebitda_ttm : Optional[Union[float]]
            Enterprise value-to-EBITDA ratio calculated as trailing twelve months.
        ev_to_operating_cash_flow_ttm : Optional[Union[float]]
            Enterprise value-to-operating cash flow ratio calculated as trailing twelve months.
        ev_to_free_cash_flow_ttm : Optional[Union[float]]
            Enterprise value-to-free cash flow ratio calculated as trailing twelve months.
        earnings_yield_ttm : Optional[Union[float]]
            Earnings yield calculated as trailing twelve months.
        free_cash_flow_yield_ttm : Optional[Union[float]]
            Free cash flow yield calculated as trailing twelve months.
        debt_to_equity_ttm : Optional[Union[float]]
            Debt-to-equity ratio calculated as trailing twelve months.
        debt_to_assets_ttm : Optional[Union[float]]
            Debt-to-assets ratio calculated as trailing twelve months.
        net_debt_to_ebitda_ttm : Optional[Union[float]]
            Net debt-to-EBITDA ratio calculated as trailing twelve months.
        current_ratio_ttm : Optional[Union[float]]
            Current ratio calculated as trailing twelve months.
        interest_coverage_ttm : Optional[Union[float]]
            Interest coverage calculated as trailing twelve months.
        income_quality_ttm : Optional[Union[float]]
            Income quality calculated as trailing twelve months.
        dividend_yield_ttm : Optional[Union[float]]
            Dividend yield calculated as trailing twelve months.
        dividend_yield_percentage_ttm : Optional[Union[float]]
            Dividend yield percentage calculated as trailing twelve months.
        dividend_to_market_cap_ttm : Optional[Union[float]]
            Dividend to market capitalization ratio calculated as trailing twelve months.
        dividend_per_share_ttm : Optional[Union[float]]
            Dividend per share calculated as trailing twelve months.
        payout_ratio_ttm : Optional[Union[float]]
            Payout ratio calculated as trailing twelve months.
        sales_general_and_administrative_to_revenue_ttm : Optional[Union[float]]
            Sales general and administrative expenses-to-revenue ratio calculated as trailing twelve months.
        research_and_development_to_revenue_ttm : Optional[Union[float]]
            Research and development expenses-to-revenue ratio calculated as trailing twelve months.
        intangibles_to_total_assets_ttm : Optional[Union[float]]
            Intangibles-to-total assets ratio calculated as trailing twelve months.
        capex_to_operating_cash_flow_ttm : Optional[Union[float]]
            Capital expenditures-to-operating cash flow ratio calculated as trailing twelve months.
        capex_to_revenue_ttm : Optional[Union[float]]
            Capital expenditures-to-revenue ratio calculated as trailing twelve months.
        capex_to_depreciation_ttm : Optional[Union[float]]
            Capital expenditures-to-depreciation ratio calculated as trailing twelve months.
        stock_based_compensation_to_revenue_ttm : Optional[Union[float]]
            Stock-based compensation-to-revenue ratio calculated as trailing twelve months.
        graham_number_ttm : Optional[Union[float]]
            Graham number calculated as trailing twelve months.
        roic_ttm : Optional[Union[float]]
            Return on invested capital calculated as trailing twelve months.
        return_on_tangible_assets_ttm : Optional[Union[float]]
            Return on tangible assets calculated as trailing twelve months.
        graham_net_net_ttm : Optional[Union[float]]
            Graham net-net working capital calculated as trailing twelve months.
        working_capital_ttm : Optional[Union[float]]
            Working capital calculated as trailing twelve months.
        tangible_asset_value_ttm : Optional[Union[float]]
            Tangible asset value calculated as trailing twelve months.
        net_current_asset_value_ttm : Optional[Union[float]]
            Net current asset value calculated as trailing twelve months.
        invested_capital_ttm : Optional[Union[float]]
            Invested capital calculated as trailing twelve months.
        average_receivables_ttm : Optional[Union[float]]
            Average receivables calculated as trailing twelve months.
        average_payables_ttm : Optional[Union[float]]
            Average payables calculated as trailing twelve months.
        average_inventory_ttm : Optional[Union[float]]
            Average inventory calculated as trailing twelve months.
        days_sales_outstanding_ttm : Optional[Union[float]]
            Days sales outstanding calculated as trailing twelve months.
        days_payables_outstanding_ttm : Optional[Union[float]]
            Days payables outstanding calculated as trailing twelve months.
        days_of_inventory_on_hand_ttm : Optional[Union[float]]
            Days of inventory on hand calculated as trailing twelve months.
        receivables_turnover_ttm : Optional[Union[float]]
            Receivables turnover calculated as trailing twelve months.
        payables_turnover_ttm : Optional[Union[float]]
            Payables turnover calculated as trailing twelve months.
        inventory_turnover_ttm : Optional[Union[float]]
            Inventory turnover calculated as trailing twelve months.
        roe_ttm : Optional[Union[float]]
            Return on equity calculated as trailing twelve months.
        capex_per_share_ttm : Optional[Union[float]]
            Capital expenditures per share calculated as trailing twelve months."""  # noqa: E501

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                "limit": limit,
            },
            extra_params=kwargs,
        )

        return self._run(
            "/stocks/multiples",
            **inputs,
        )

    @validate_call
    def news(
        self,
        symbols: typing_extensions.Annotated[
            str, OpenBBCustomParameter(description="Comma separated list of symbols.")
        ],
        limit: typing_extensions.Annotated[
            Union[typing_extensions.Annotated[int, Ge(ge=0)], None],
            OpenBBCustomParameter(description="Number of results to return per page."),
        ] = 20,
        provider: Union[Literal["benzinga", "fmp", "intrinio", "polygon"], None] = None,
        **kwargs
    ) -> OBBject[List[Data]]:
        """Get news for one or more stock tickers.

        Parameters
        ----------
        symbols : str
            Comma separated list of symbols.
        limit : Union[typing_extensions.Annotated[int, Ge(ge=0)], None]
            Number of results to return per page.
        provider : Union[Literal['benzinga', 'fmp', 'intrinio', 'polygon'], None]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'benzinga' if there is
            no default.
        display : Literal['headline', 'abstract', 'full']
            Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga)
        date : Optional[Union[str]]
            Date of the news to retrieve. (provider: benzinga)
        start_date : Optional[Union[str]]
            Start date of the news to retrieve. (provider: benzinga)
        end_date : Optional[Union[str]]
            End date of the news to retrieve. (provider: benzinga)
        updated_since : Optional[Union[int]]
            Number of seconds since the news was updated. (provider: benzinga)
        published_since : Optional[Union[int]]
            Number of seconds since the news was published. (provider: benzinga)
        sort : Optional[Union[Literal['id', 'created', 'updated']]]
            Key to sort the news by. (provider: benzinga)
        order : Optional[Union[Literal['asc', 'desc']]]
            Order to sort the news by. (provider: benzinga); Sort order of the articles. (provider: polygon)
        isin : Optional[Union[str]]
            The ISIN of the news to retrieve. (provider: benzinga)
        cusip : Optional[Union[str]]
            The CUSIP of the news to retrieve. (provider: benzinga)
        channels : Optional[Union[str]]
            Channels of the news to retrieve. (provider: benzinga)
        topics : Optional[Union[str]]
            Topics of the news to retrieve. (provider: benzinga)
        authors : Optional[Union[str]]
            Authors of the news to retrieve. (provider: benzinga)
        content_types : Optional[Union[str]]
            Content types of the news to retrieve. (provider: benzinga)
        published_utc : Optional[Union[str]]
            Date query to fetch articles. Supports operators <, <=, >, >= (provider: polygon)

        Returns
        -------
        OBBject
            results : Union[List[StockNews]]
                Serializable results.
            provider : Union[Literal['benzinga', 'fmp', 'intrinio', 'polygon'], None]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        StockNews
        ---------
        date : datetime
            Published date of the news.
        title : str
            Title of the news.
        image : Optional[Union[str]]
            Image URL of the news.
        text : Optional[Union[str]]
            Text/body of the news.
        url : str
            URL of the news.
        id : Optional[Union[str]]
            ID of the news. (provider: benzinga); Intrinio ID for the article. (provider: intrinio); Article ID. (provider: polygon)
        author : Optional[Union[str]]
            Author of the news. (provider: benzinga); Author of the article. (provider: polygon)
        teaser : Optional[Union[str]]
            Teaser of the news. (provider: benzinga)
        images : Optional[Union[List[Dict[str, str]]]]
            Images associated with the news. (provider: benzinga)
        channels : Optional[Union[str]]
            Channels associated with the news. (provider: benzinga)
        stocks : Optional[Union[str]]
            Stocks associated with the news. (provider: benzinga)
        tags : Optional[Union[str]]
            Tags associated with the news. (provider: benzinga)
        updated : Optional[Union[datetime]]
            None
        symbol : Optional[Union[str]]
            Ticker of the fetched news. (provider: fmp)
        site : Optional[Union[str]]
            Name of the news source. (provider: fmp)
        amp_url : Optional[Union[str]]
            AMP URL. (provider: polygon)
        image_url : Optional[Union[str]]
            Image URL. (provider: polygon)
        keywords : Optional[Union[List[str]]]
            Keywords in the article (provider: polygon)
        publisher : Optional[Union[openbb_polygon.models.stock_news.PolygonPublisher]]
            Publisher of the article. (provider: polygon)
        tickers : Optional[Union[List[str]]]
            Tickers covered in the article. (provider: polygon)"""  # noqa: E501

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbols": symbols,
                "limit": limit,
            },
            extra_params=kwargs,
        )

        return self._run(
            "/stocks/news",
            **inputs,
        )

    @property
    def options(self):  # route = "/stocks/options"
        from . import stocks_options

        return stocks_options.ROUTER_stocks_options(command_runner=self._command_runner)

    @validate_call
    def quote(
        self,
        symbol: typing_extensions.Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Comma separated list of symbols."),
        ] = None,
        provider: Union[Literal["fmp", "intrinio"], None] = None,
        **kwargs
    ) -> OBBject[Union[List[Data], Data]]:
        """Load stock data for a specific ticker.

        Parameters
        ----------
        symbol : str
            Comma separated list of symbols.
        provider : Union[Literal['fmp', 'intrinio'], None]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        source : Literal['iex', 'bats', 'bats_delayed', 'utp_delayed', 'cta_a_delayed', 'cta_b_delayed', 'intrinio_mx', 'intrinio_mx_plus', 'delayed_sip']
            Source of the data. (provider: intrinio)

        Returns
        -------
        OBBject
            results : Union[List[StockQuote], StockQuote]
                Serializable results.
            provider : Union[Literal['fmp', 'intrinio'], None]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        StockQuote
        ----------
        day_low : Optional[Union[float]]
            Lowest price of the stock in the current trading day.
        day_high : Optional[Union[float]]
            Highest price of the stock in the current trading day.
        date : Optional[Union[datetime]]
            Timestamp of the stock quote.
        symbol : Optional[Union[str]]
            Symbol of the company. (provider: fmp)
        name : Optional[Union[str]]
            Name of the company. (provider: fmp)
        price : Optional[Union[float]]
            Current trading price of the stock. (provider: fmp)
        changes_percentage : Optional[Union[float]]
            Change percentage of the stock price. (provider: fmp)
        change : Optional[Union[float]]
            Change in the stock price. (provider: fmp)
        year_high : Optional[Union[float]]
            Highest price of the stock in the last 52 weeks. (provider: fmp)
        year_low : Optional[Union[float]]
            Lowest price of the stock in the last 52 weeks. (provider: fmp)
        market_cap : Optional[Union[float]]
            Market cap of the company. (provider: fmp)
        price_avg50 : Optional[Union[float]]
            50 days average price of the stock. (provider: fmp)
        price_avg200 : Optional[int]
            200 days average price of the stock. (provider: fmp)
        volume : Optional[int]
            Volume of the stock in the current trading day. (provider: fmp)
        avg_volume : Optional[int]
            Average volume of the stock in the last 10 trading days. (provider: fmp)
        exchange : Optional[Union[str]]
            Exchange the stock is traded on. (provider: fmp)
        open : Optional[Union[float]]
            Opening price of the stock in the current trading day. (provider: fmp)
        previous_close : Optional[Union[float]]
            Previous closing price of the stock. (provider: fmp)
        eps : Optional[Union[float]]
            Earnings per share of the stock. (provider: fmp)
        pe : Optional[Union[float]]
            Price earnings ratio of the stock. (provider: fmp)
        earnings_announcement : Optional[Union[str]]
            Earnings announcement date of the stock. (provider: fmp)
        shares_outstanding : Optional[int]
            Number of shares outstanding of the stock. (provider: fmp)
        last_price : Optional[Union[float]]
            Price of the last trade. (provider: intrinio)
        last_time : Optional[Union[datetime]]
            Date and Time when the last trade occurred. (provider: intrinio)
        last_size : Optional[Union[int]]
            Size of the last trade. (provider: intrinio)
        bid_price : Optional[Union[float]]
            Price of the top bid order. (provider: intrinio)
        bid_size : Optional[Union[int]]
            Size of the top bid order. (provider: intrinio)
        ask_price : Optional[Union[float]]
            Price of the top ask order. (provider: intrinio)
        ask_size : Optional[Union[int]]
            Size of the top ask order. (provider: intrinio)
        open_price : Optional[Union[float]]
            Open price for the trading day. (provider: intrinio)
        close_price : Optional[Union[float]]
            Closing price for the trading day (IEX source only). (provider: intrinio)
        high_price : Optional[Union[float]]
            High Price for the trading day. (provider: intrinio)
        low_price : Optional[Union[float]]
            Low Price for the trading day. (provider: intrinio)
        exchange_volume : Optional[Union[int]]
            Number of shares exchanged during the trading day on the exchange. (provider: intrinio)
        market_volume : Optional[Union[int]]
            Number of shares exchanged during the trading day for the whole market. (provider: intrinio)
        updated_on : Optional[Union[datetime]]
            Date and Time when the data was last updated. (provider: intrinio)
        source : Optional[Union[str]]
            Source of the data. (provider: intrinio)
        listing_venue : Optional[Union[str]]
            Listing venue where the trade took place (SIP source only). (provider: intrinio)
        sales_conditions : Optional[Union[str]]
            Indicates any sales condition modifiers associated with the trade. (provider: intrinio)
        quote_conditions : Optional[Union[str]]
            Indicates any quote condition modifiers associated with the trade. (provider: intrinio)
        market_center_code : Optional[Union[str]]
            Market center character code. (provider: intrinio)
        is_darkpool : Optional[Union[bool]]
            Whether or not the current trade is from a darkpool. (provider: intrinio)
        messages : Optional[Union[List[str]]]
            Messages associated with the endpoint. (provider: intrinio)
        security : Optional[Union[Dict[str, Any]]]
            Security details related to the quote. (provider: intrinio)"""  # noqa: E501

        inputs = filter_inputs(
            provider_choices={
                "provider": provider,
            },
            standard_params={
                "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
            },
            extra_params=kwargs,
        )

        return self._run(
            "/stocks/quote",
            **inputs,
        )