"""Blockchain Center View"""
import logging
import os
from datetime import datetime
from typing import Optional, Union

from openbb_terminal import OpenBBFigure
from openbb_terminal.config_terminal import theme
from openbb_terminal.cryptocurrency.overview.blockchaincenter_model import (
    DAYS,
    get_altcoin_index,
)
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def display_altcoin_index(
    period: int = 365,
    start_date: str = "2010-01-01",
    end_date: Optional[str] = None,
    export: str = "",
    sheet_name: Optional[str] = None,
    external_axes: bool = False,
) -> Union[OpenBBFigure, None]:
    """Displays altcoin index overtime
    [Source: https://blockchaincenter.net]

    Parameters
    ----------
    start_date : str
        Initial date, format YYYY-MM-DD
    end_date : Optional[str]
        Final date, format YYYY-MM-DD
    period: int
        Number of days to check the performance of coins and calculate the altcoin index.
        E.g., 365 will check yearly performance , 90 will check seasonal performance (90 days),
        30 will check monthly performance (30 days).
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : bool, optional
        Whether to return the figure object or not, by default False
    """

    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")

    if period in DAYS:
        df = get_altcoin_index(period, start_date, end_date)

        if df.empty:
            return console.print("\nError scraping blockchain central\n")

        fig = OpenBBFigure(yaxis_title="Altcoin Index")
        fig.set_title(f"Altcoin Index (Performance based on {period} days)")
        fig.add_scatter(x=df.index, y=df["Value"], mode="lines", name="Altcoin Index")

        fig.add_hline(
            y=75,
            line_color=theme.up_color,
            annotation=dict(
                text="Altcoin Season (75)",
                x=0.5,
                xanchor="center",
            ),
        )
        fig.add_hline(
            y=25,
            line_color=theme.down_color,
            annotation=dict(
                text="Bitcoin Season (25)",
                x=0.5,
                xanchor="center",
                yshift=-30,
            ),
        )

        export_data(
            export,
            os.path.dirname(os.path.abspath(__file__)),
            "altindex",
            df,
            sheet_name,
            fig,
        )

        return fig.show(external=external_axes)

    return None
