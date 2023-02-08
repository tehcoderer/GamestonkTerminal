"""Custom TA indicators"""
__docformat__ = "numpy"

import logging
import os
from typing import Optional, Union

import pandas as pd

from openbb_terminal.common.technical_analysis import (
    ta_helpers,
)
from openbb_terminal.core.plots.plotly_ta.ta_class import OpenBBFigure, PlotlyTA
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    export_data,
    print_rich_table,
)

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def fibonacci_retracement(
    data: pd.DataFrame,
    limit: int = 120,
    start_date: Optional[Union[str, None]] = None,
    end_date: Optional[Union[str, None]] = None,
    symbol: str = "",
    export: str = "",
    sheet_name: Optional[str] = None,
    external_axes: bool = False,
) -> Union[None, OpenBBFigure]:
    """Plots Calculated fibonacci retracement levels

    Parameters
    ----------
    data: pd.DataFrame
        OHLC data
    limit: int
        Days to lookback
    start_date: Optional[str, None]
        User picked date for starting retracement
    end_date: Optional[str, None]
        User picked date for ending retracement
    symbol: str
        Ticker symbol
    sheet_name: str
        Optionally specify the name of the sheet the data is exported to.
    export: str
        Format to export data
    external_axes : bool, optional
        Whether to return the figure object or not, by default False

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> df = openbb.stocks.load(symbol="aapl")
    >>> openbb.ta.fib_chart(data=df)
    """
    data = pd.DataFrame(data)
    data.index.name = "date"

    close_col = ta_helpers.check_columns(data)
    if close_col is None:
        return None

    ta = PlotlyTA()
    fig = ta.plot(
        data,
        dict(fib=dict(limit=limit, start_date=start_date, end_date=end_date)),
        f"Fibonacci Support for {symbol.upper()}",
        False,
        volume=False,
    )

    if not external_axes:
        print_rich_table(
            ta.df_fib,
            headers=["Fib Level", "Price"],
            show_index=False,
            title="Fibonacci retracement levels",
        )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)).replace("common", "stocks"),
        "fib",
        ta.df_ta,
        sheet_name,
    )

    return fig.show(external=external_axes)
