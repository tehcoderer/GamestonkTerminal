"""Intrinio View Functions"""
__docformat__ = "numpy"

import logging
import os
from typing import Optional, Union

from openbb_terminal import OpenBBFigure, theme
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    print_rich_table,
)
from openbb_terminal.rich_config import console
from openbb_terminal.stocks.options import intrinio_model

logger = logging.getLogger(__name__)

# pylint: disable=too-many-arguments


@log_start_end(log=logger)
def display_historical(
    symbol: str,
    expiry: str,
    strike: float = 0,
    put: bool = False,
    raw: bool = False,
    chain_id: Optional[str] = None,
    export: str = "",
    sheet_name: Optional[str] = None,
    external_axes: bool = False,
) -> Union[None, OpenBBFigure]:
    """Plot historical option prices

    Parameters
    ----------
    symbol: str
        Stock ticker symbol
    expiry: str
        Expiry date of option
    strike: float
        Option strike price
    put: bool
        Is this a put option?
    raw: bool
        Print raw data
    chain_id: str
        OCC option symbol
    export: str
        Format of export file
    sheet_name: str
        Optionally specify the name of the sheet to export to
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """
    op_type = ["Call", "Put"][put]
    if chain_id is not None:
        df_hist = intrinio_model.get_historical_options(chain_id)
    else:
        chain_id = f"{symbol}{''.join(expiry[2:].split('-'))}{'P' if put else 'C'}{str(int(1000*strike)).zfill(8)}"
        df_hist = intrinio_model.get_historical_options(chain_id)

    if raw:
        print_rich_table(
            df_hist,
            headers=[x.title() for x in df_hist.columns],
            title="Historical Option Prices",
            export=bool(export),
        )

    df_hist.columns = [x.title() for x in df_hist.columns]

    fig = OpenBBFigure.create_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.3, 0.7],
        subplot_titles=[f"{symbol} {strike} {op_type}", "Volume"],
    )

    fig.add_candlestick(
        open=df_hist["Open"],
        high=df_hist["High"],
        low=df_hist["Low"],
        close=df_hist["Close"],
        x=df_hist.index,
        name=f"{symbol} OHLC",
        row=1,
        col=1,
    )
    fig.add_stock_volume(df_hist, row=2, col=1)
    fig.hide_holidays()

    if export:
        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "hist",
            df_hist,
            sheet_name,
            fig,
        )

    return fig.show(external=external_axes)


@log_start_end(log=logger)
def view_historical_greeks(
    symbol: str,
    expiry: str,
    strike: Union[float, str],
    greek: str = "Delta",
    chain_id: str = "",
    put: bool = False,
    raw: bool = False,
    limit: Union[int, str] = 20,
    export: str = "",
    sheet_name: Optional[str] = None,
    external_axes: bool = False,
) -> Union[None, OpenBBFigure]:
    """Plots historical greeks for a given option. [Source: Syncretism]

    Parameters
    ----------
    symbol: str
        Stock ticker
    expiry: str
        Expiration date
    strike: Union[str, float]
        Strike price to consider
    greek: str
        Greek variable to plot
    chain_id: str
        OCC option chain.  Overwrites other variables
    put: bool
        Is this a put option?
    raw: bool
        Print to console
    limit: int
        Number of rows to show in raw
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """

    if chain_id:
        df = intrinio_model.get_historical_options(chain_id)
        title = f"{(greek).capitalize()} historical for {chain_id}"
    else:
        chain_id = f"{symbol}{''.join(expiry[2:].split('-'))}{'P' if put else 'C'}{str(int(1000*strike)).zfill(8)}"
        df = intrinio_model.get_historical_options(chain_id)
        title = f"{(greek).capitalize()} historical for {symbol.upper()} {strike} {['Call','Put'][put]}"

    if df.empty:
        return None

    df = df.rename(columns={"impliedVolatility": "iv", "close": "price"})

    if isinstance(limit, str):
        try:
            limit = int(limit)
        except ValueError:
            return console.print(
                f"[red]Could not convert limit of {limit} to a number.[/red]\n"
            )

    if raw:
        print_rich_table(
            df.tail(limit),
            headers=list(df.columns),
            title="Historical Greeks",
            show_index=True,
            export=bool(export),
        )

    try:
        greek_df = df[greek.lower()]
    except KeyError:
        return console.print(f"[red]Could not find greek {greek} in data.[/red]\n")

    fig = OpenBBFigure.create_subplots(
        shared_xaxes=True,
        specs=[[{"secondary_y": True}]],
        vertical_spacing=0.03,
        horizontal_spacing=0.1,
    )
    fig.set_title(title)

    fig.add_scatter(
        x=df.index,
        y=df.price,
        name="Stock Price",
        line=dict(color=theme.down_color),
    )
    fig.add_scatter(
        x=df.index,
        y=greek_df,
        name=greek.title(),
        line=dict(color=theme.up_color),
        yaxis="y2",
    )
    fig.update_layout(
        yaxis2=dict(
            side="left",
            title=greek,
            anchor="x",
            overlaying="y",
        ),
        yaxis=dict(
            title=f"{symbol} Price",
            side="right",
        ),
    )
    fig.hide_holidays()

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "grhist",
        df,
        sheet_name,
        fig,
    )

    return fig.show(external=external_axes)
