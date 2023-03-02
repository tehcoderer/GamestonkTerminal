""" Business Insider View """
__docformat__ = "numpy"

import logging
import os
import textwrap
from datetime import datetime, timedelta
from typing import Optional, Union

from pandas.core.frame import DataFrame

from openbb_terminal import OpenBBFigure
from openbb_terminal.common.technical_analysis import ta_helpers
from openbb_terminal.config_terminal import theme
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    print_rich_table,
)
from openbb_terminal.rich_config import console
from openbb_terminal.stocks.fundamental_analysis import business_insider_model
from openbb_terminal.stocks.stocks_helper import load

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_management(symbol: str, export: str = "", sheet_name: Optional[str] = None):
    """Display company's managers

    Parameters
    ----------
    symbol : str
        Stock ticker symbol
    export : str
        Format to export data
    """
    df_management = business_insider_model.get_management(symbol)

    df_new = df_management.applymap(
        lambda x: "\n".join(textwrap.wrap(x, width=30)) if isinstance(x, str) else x
    )

    if not df_new.empty:
        print_rich_table(
            df_new,
            title="Company Managers",
            headers=list(df_new.columns),
            show_index=True,
            index_name="Name",
            export=bool(export),
        )

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "mgmt",
            df_management,
            sheet_name,
        )
    else:
        logger.error("Data not available")


@log_start_end(log=logger)
def price_target_from_analysts(
    symbol: str,
    data: Optional[DataFrame] = None,
    start_date: Optional[str] = None,
    limit: int = 10,
    raw: bool = False,
    export: str = "",
    sheet_name: Optional[str] = None,
    external_axes: bool = False,
) -> Union[OpenBBFigure, None]:
    """Display analysts' price targets for a given stock. [Source: Business Insider]

    Parameters
    ----------
    symbol: str
        Due diligence ticker symbol
    data: Optional[DataFrame]
        Price target DataFrame
    start_date : Optional[str]
        Start date of the stock data, format YYYY-MM-DD
    limit : int
        Number of latest price targets from analysts to print
    raw: bool
        Display raw data only
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Export dataframe data to csv,json,xlsx file
    external_axes: bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> openbb.stocks.fa.pt_chart(symbol="AAPL")
    """

    if start_date is None:
        start_date = (datetime.now() - timedelta(days=1100)).strftime("%Y-%m-%d")

    if data is None:
        data = load(symbol=symbol, start_date=start_date)

    df_analyst_data = business_insider_model.get_price_target_from_analysts(symbol)
    if df_analyst_data.empty:
        return console.print("[red]Could not get data for ticker.[/red]\n")

    fig = OpenBBFigure(yaxis_title="Share Price").set_title(
        f"{symbol} (Time Series) and Price Target"
    )
    close_col = ta_helpers.check_columns(data, False, False)
    df_analyst_plot = df_analyst_data.copy()

    # Slice start of ratings
    if start_date:
        df_analyst_plot = df_analyst_plot[start_date:]  # type: ignore

    fig.add_scatter(
        x=data.index,
        y=data[close_col].values,
        name="Close",
        line_width=2,
    )

    df_grouped = df_analyst_plot.groupby(by=["Date"]).mean(numeric_only=True)

    fig.add_scatter(
        x=df_grouped.index,
        y=df_grouped.values,
        name="Average Price Target",
    )

    fig.add_scatter(
        x=df_analyst_plot.index,
        y=df_analyst_plot["Price Target"].values,
        name="Price Target",
        mode="markers+lines",
        marker=dict(
            color=theme.down_color,
            line=dict(color=theme.up_color, width=1),
            size=10,
        ),
        line=dict(color=theme.get_colors()[1]),
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "pt",
        df_analyst_data,
        sheet_name,
        fig,
    )

    if raw:
        df_analyst_data.index = df_analyst_data.index.strftime("%Y-%m-%d")
        return print_rich_table(
            df_analyst_data.sort_index(ascending=False).head(limit),
            headers=list(df_analyst_data.columns),
            show_index=True,
            title="Analyst Price Targets",
            export=bool(export),
        )

    return fig.show(external=external_axes)


@log_start_end(log=logger)
def estimates(
    symbol: str, estimate: str, export: str = "", sheet_name: Optional[str] = None
):
    """Display analysts' estimates for a given ticker. [Source: Business Insider]

    Parameters
    ----------
    symbol : str
        Ticker to get analysts' estimates
    estimate: str
        Type of estimate to get
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    (
        df_year_estimates,
        df_quarter_earnings,
        df_quarter_revenues,
    ) = business_insider_model.get_estimates(symbol)

    if estimate == "annualearnings":
        print_rich_table(
            df_year_estimates,
            headers=list(df_year_estimates.columns),
            show_index=True,
            title="Annual Earnings Estimates",
            export=bool(export),
        )
        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "pt_year",
            df_year_estimates,
            sheet_name,
        )

    elif estimate == "quarterearnings":
        print_rich_table(
            df_quarter_earnings,
            headers=list(df_quarter_earnings.columns),
            show_index=True,
            title="Quarterly Earnings Estimates",
            export=bool(export),
        )
        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "pt_qtr_earnings",
            df_quarter_earnings,
            sheet_name,
        )

    elif estimate == "annualrevenue":
        print_rich_table(
            df_quarter_revenues,
            headers=list(df_quarter_revenues.columns),
            show_index=True,
            title="Quarterly Revenue Estimates",
            export=bool(export),
        )

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "pt_qtr_revenues",
            df_quarter_revenues,
            sheet_name,
        )
    else:
        console.print("[red]Invalid estimate type[/red]")
