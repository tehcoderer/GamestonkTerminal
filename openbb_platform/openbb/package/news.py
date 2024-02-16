### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Optional, Union

from annotated_types import Ge
from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated


class ROUTER_news(Container):
    """/news
    company
    world
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def company(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(
                description="Symbol to get data for. This endpoint will accept multiple symbols separated by commas. Multiple items allowed: benzinga, intrinio."
            ),
        ],
        limit: Annotated[
            Optional[Annotated[int, Ge(ge=0)]],
            OpenBBCustomParameter(description="The number of data entries to return."),
        ] = 20,
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
        provider: Optional[
            Literal["benzinga", "fmp", "intrinio", "polygon", "tiingo", "yfinance"]
        ] = None,
        **kwargs
    ) -> OBBject:
        """Company News. Get news for one or more companies.

        Parameters
        ----------
        symbol : Union[str, List[str]]
            Symbol to get data for. This endpoint will accept multiple symbols separated by commas. Multiple items allowed: benzinga, intrinio.
        limit : Optional[Annotated[int, Ge(ge=0)]]
            The number of data entries to return.
        start_date : Union[datetime.date, None, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, None, str]
            End date of the data, in YYYY-MM-DD format.
        provider : Optional[Literal['benzinga', 'fmp', 'intrinio', 'polygon', 'tiing...
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'benzinga' if there is
            no default.
        date : Optional[datetime.date]
            A specific date to get data for. (provider: benzinga)
        display : Literal['headline', 'abstract', 'full']
            Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga)
        updated_since : Optional[int]
            Number of seconds since the news was updated. (provider: benzinga)
        published_since : Optional[int]
            Number of seconds since the news was published. (provider: benzinga)
        sort : Literal['id', 'created', 'updated']
            Key to sort the news by. (provider: benzinga)
        order : Optional[Literal['asc', 'desc']]
            Order to sort the news by. (provider: benzinga);
            Sort order of the articles. (provider: polygon)
        isin : Optional[str]
            The company's ISIN. (provider: benzinga)
        cusip : Optional[str]
            The company's CUSIP. (provider: benzinga)
        channels : Optional[str]
            Channels of the news to retrieve. (provider: benzinga)
        topics : Optional[str]
            Topics of the news to retrieve. (provider: benzinga)
        authors : Optional[str]
            Authors of the news to retrieve. (provider: benzinga)
        content_types : Optional[str]
            Content types of the news to retrieve. (provider: benzinga)
        page : Optional[int]
            Page number of the results. Use in combination with limit. (provider: fmp)
        published_utc : Optional[str]
            Date query to fetch articles. Supports operators <, <=, >, >= (provider: polygon)
        source : Optional[str]
            A comma-separated list of the domains requested. (provider: tiingo)

        Returns
        -------
        OBBject
            results : List[CompanyNews]
                Serializable results.
            provider : Optional[Literal['benzinga', 'fmp', 'intrinio', 'polygon', 'tiingo', 'yfinance']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        CompanyNews
        -----------
        symbols : str
             Here it is a separated list of symbols.
        date : datetime
            The date of the data. Here it is the date of the news.
        title : str
            Title of the news.
        image : Optional[str]
            Image URL of the news.
        text : Optional[str]
            Text/body of the news.
        url : str
            URL of the news.
        id : Optional[str]
            Article ID. (provider: benzinga, intrinio, polygon)
        author : Optional[str]
            Author of the article. (provider: benzinga, polygon)
        teaser : Optional[str]
            Teaser of the news. (provider: benzinga)
        images : Optional[Union[List[Dict[str, str]], List[str], str]]
            URL to the images of the news. (provider: benzinga, fmp)
        channels : Optional[str]
            Channels associated with the news. (provider: benzinga)
        stocks : Optional[str]
            Stocks associated with the news. (provider: benzinga)
        tags : Optional[str]
            Tags associated with the news. (provider: benzinga, tiingo)
        updated : Optional[datetime]
            Updated date of the news. (provider: benzinga)
        site : Optional[str]
            Name of the news source. (provider: fmp);
            News source. (provider: tiingo)
        amp_url : Optional[str]
            AMP URL. (provider: polygon)
        image_url : Optional[str]
            Image URL. (provider: polygon)
        keywords : Optional[List[str]]
            Keywords in the article (provider: polygon)
        publisher : Optional[Union[openbb_polygon.models.company_news.PolygonPublisher, str]]
            Publisher of the article. (provider: polygon, yfinance)
        article_id : Optional[int]
            Unique ID of the news article. (provider: tiingo)
        crawl_date : Optional[datetime]
            Date the news article was crawled. (provider: tiingo)
        uuid : Optional[str]
            Unique identifier for the news article (provider: yfinance)
        type : Optional[str]
            Type of the news article (provider: yfinance)
        thumbnail : Optional[List]
            Thumbnail related data to the ticker news article. (provider: yfinance)

        Example
        -------
        >>> from openbb import obb
        >>> obb.news.company(symbol="AAPL", limit=20)
        >>> # Get news on the specified dates.
        >>> obb.news.company(symbol='AAPL', start_date='2024-02-01', end_date='2024-02-07')
        >>> # Display the headlines of the news.
        >>> obb.news.company(symbol='AAPL', display='headline', provider='benzinga')
        >>> # Get news for multiple symbols.
        >>> obb.news.company(symbol='aapl,tsla')
        >>> # Get news company's ISIN.
        >>> obb.news.company(symbol='NVDA', isin='US0378331005')
        """  # noqa: E501

        return self._run(
            "/news/company",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/news/company",
                        (
                            "benzinga",
                            "fmp",
                            "intrinio",
                            "polygon",
                            "tiingo",
                            "yfinance",
                        ),
                    )
                },
                standard_params={
                    "symbol": symbol,
                    "limit": limit,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                extra_params=kwargs,
                extra_info={
                    "symbol": {"multiple_items_allowed": ["benzinga", "intrinio"]}
                },
            )
        )

    @validate
    def world(
        self,
        limit: Annotated[
            int,
            OpenBBCustomParameter(
                description="The number of data entries to return. The number of articles to return."
            ),
        ] = 2500,
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
        provider: Optional[Literal["benzinga", "fmp", "intrinio", "tiingo"]] = None,
        **kwargs
    ) -> OBBject:
        """World News. Global news data.

        Parameters
        ----------
        limit : int
            The number of data entries to return. The number of articles to return.
        start_date : Union[datetime.date, None, str]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Union[datetime.date, None, str]
            End date of the data, in YYYY-MM-DD format.
        provider : Optional[Literal['benzinga', 'fmp', 'intrinio', 'tiingo']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'benzinga' if there is
            no default.
        date : Optional[datetime.date]
            A specific date to get data for. (provider: benzinga)
        display : Literal['headline', 'abstract', 'full']
            Specify headline only (headline), headline + teaser (abstract), or headline + full body (full). (provider: benzinga)
        updated_since : Optional[int]
            Number of seconds since the news was updated. (provider: benzinga)
        published_since : Optional[int]
            Number of seconds since the news was published. (provider: benzinga)
        sort : Literal['id', 'created', 'updated']
            Key to sort the news by. (provider: benzinga)
        order : Literal['asc', 'desc']
            Order to sort the news by. (provider: benzinga)
        isin : Optional[str]
            The ISIN of the news to retrieve. (provider: benzinga)
        cusip : Optional[str]
            The CUSIP of the news to retrieve. (provider: benzinga)
        channels : Optional[str]
            Channels of the news to retrieve. (provider: benzinga)
        topics : Optional[str]
            Topics of the news to retrieve. (provider: benzinga)
        authors : Optional[str]
            Authors of the news to retrieve. (provider: benzinga)
        content_types : Optional[str]
            Content types of the news to retrieve. (provider: benzinga)
        offset : Optional[int]
            Page offset, used in conjunction with limit. (provider: tiingo)
        source : Optional[str]
            A comma-separated list of the domains requested. (provider: tiingo)

        Returns
        -------
        OBBject
            results : List[WorldNews]
                Serializable results.
            provider : Optional[Literal['benzinga', 'fmp', 'intrinio', 'tiingo']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        WorldNews
        ---------
        date : datetime
            The date of the data. The published date of the article.
        title : str
            Title of the article.
        images : Optional[List[Dict[str, str]]]
            Images associated with the article.
        text : Optional[str]
            Text/body of the article.
        url : Optional[str]
            URL to the article.
        id : Optional[str]
            Article ID. (provider: benzinga, intrinio)
        author : Optional[str]
            Author of the news. (provider: benzinga)
        teaser : Optional[str]
            Teaser of the news. (provider: benzinga)
        channels : Optional[str]
            Channels associated with the news. (provider: benzinga)
        stocks : Optional[str]
            Stocks associated with the news. (provider: benzinga)
        tags : Optional[str]
            Tags associated with the news. (provider: benzinga, tiingo)
        updated : Optional[datetime]
            Updated date of the news. (provider: benzinga)
        site : Optional[str]
            News source. (provider: fmp, tiingo)
        company : Optional[Dict[str, Any]]
            Company details related to the news article. (provider: intrinio)
        symbols : Optional[str]
            Ticker tagged in the fetched news. (provider: tiingo)
        article_id : Optional[int]
            Unique ID of the news article. (provider: tiingo)
        crawl_date : Optional[datetime]
            Date the news article was crawled. (provider: tiingo)

        Example
        -------
        >>> from openbb import obb
        >>> obb.news.world(limit=2500)
        >>> # Get news on the specified dates.
        >>> obb.news.world(start_date='2024-02-01', end_date='2024-02-07')
        >>> # Display the headlines of the news.
        >>> obb.news.world(display='headline', provider='benzinga')
        >>> # Get news by topics.
        >>> obb.news.world(topics='finance', provider='benzinga')
        >>> # Get news by source using 'tingo' as provider.
        >>> obb.news.world(provider='tiingo', source='bloomberg')
        >>> # Filter aticles by term using 'biztoc' as provider.
        >>> obb.news.world(provider='biztoc', term='apple')
        """  # noqa: E501

        return self._run(
            "/news/world",
            **filter_inputs(
                provider_choices={
                    "provider": self._get_provider(
                        provider,
                        "/news/world",
                        ("benzinga", "fmp", "intrinio", "tiingo"),
                    )
                },
                standard_params={
                    "limit": limit,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                extra_params=kwargs,
            )
        )
