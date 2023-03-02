import pandas as pd

from openbb_terminal import OpenBBFigure, theme
from openbb_terminal.core.plots.plotly_ta.base import PltTA, indicator
from openbb_terminal.core.plots.plotly_ta.data_classes import columns_regex


class Volatility(PltTA):
    """Volatility technical indicators"""

    __inchart__ = ["bbands", "donchian", "kc"]
    __subplots__ = ["atr"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @indicator()
    def plot_atr(self, fig: OpenBBFigure, df_ta: pd.DataFrame, subplot_row: int):
        """Adds average true range to plotly figure"""

        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'ATR')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "ATR")[0]].values,
            mode="lines",
            line=dict(width=1, color=theme.get_colors()[1]),
            row=subplot_row,
            col=1,
        )

        fig.add_annotation(
            xref=f"x{subplot_row} domain",
            yref=f"y{subplot_row} domain",
            text="<b>ATR</b>",
            x=0,
            xanchor="right",
            xshift=-6,
            y=0.98,
            font_size=14,
            font_color=theme.get_colors()[1],
        )
        fig["layout"][f"yaxis{subplot_row}"].update(nticks=5, autorange=True)

        return fig, subplot_row + 1

    @indicator()
    def plot_bbands(self, fig: OpenBBFigure, df_ta: pd.DataFrame, inchart_index: int):
        """Adds bollinger bands to plotly figure"""

        bbands_opacity = 0.8 if theme.plt_style == "light" else 1

        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'BBU')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "BBU")[0]].values,
            opacity=bbands_opacity,
            mode="lines",
            line=dict(width=1, color=theme.up_color),
            row=1,
            col=1,
        )
        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'BBL')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "BBL")[0]].values,
            opacity=bbands_opacity,
            mode="lines",
            line=dict(width=1, color=theme.down_color),
            row=1,
            col=1,
        )
        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'BBM')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "BBM")[0]].values,
            opacity=1,
            mode="lines",
            line=dict(width=1, color=theme.get_colors()[1], dash="dash"),
            row=1,
            col=1,
        )
        bbands_text = (
            columns_regex(df_ta, "BBL")[0]
            .replace("BBL_", "BB")
            .replace("_", ",")
            .split(".")[0]
        )
        fig.add_annotation(
            xref="paper",
            yref="paper",
            text=f"<b>{bbands_text}</b>",
            x=0,
            xanchor="left",
            yshift=-inchart_index * 18,
            xshift=-60,
            y=0.98,
            font_size=14,
            font_color=theme.get_colors()[1],
            opacity=0.9,
        )

        return fig, inchart_index + 1

    @indicator()
    def plot_donchian(self, fig: OpenBBFigure, df_ta: pd.DataFrame, inchart_index: int):
        """Adds donchian channels to plotly figure"""

        if theme.plt_style == "light":
            fillcolor = "rgba(239, 103, 137, 0.05)"
            donchian_opacity = 0.4
        else:
            fillcolor = "rgba(239, 103, 137, 0.05)"
            donchian_opacity = 0.4

        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'DCU')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "DCU")[0]].values,
            opacity=donchian_opacity,
            mode="lines",
            line=dict(width=0.3, color="#EF6689"),
            row=1,
            col=1,
        )
        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'DCL')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "DCL")[0]].values,
            opacity=donchian_opacity,
            mode="lines",
            line=dict(width=0.3, color="#EF6689"),
            fill="tonexty",
            fillcolor=fillcolor,
            row=1,
            col=1,
        )
        fig.add_annotation(
            xref="paper",
            yref="paper",
            text=(
                f"<b>DC{self.params['donchian'].get_argument_values('upper_length') or ''},"
                f"{self.params['donchian'].get_argument_values('lower_length') or ''}</b>"
            ),
            x=0,
            xanchor="left",
            yshift=-inchart_index * 18,
            xshift=-60,
            y=0.98,
            font_size=14,
            font_color="#B47DA0",
            opacity=0.9,
        )

        return fig, inchart_index + 1

    @indicator()
    def plot_kc(self, fig: OpenBBFigure, df_ta: pd.DataFrame, inchart_index: int):
        """Adds Keltner channels to plotly figure"""

        if theme.plt_style == "light":
            fillcolor = "rgba(239, 103, 137, 0.05)"
            kc_opacity = 0.4
        else:
            fillcolor = "rgba(239, 103, 137, 0.05)"
            kc_opacity = 0.4

        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'KCU')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "KCU")[0]].values,
            opacity=kc_opacity,
            mode="lines",
            line=dict(width=0.3, color="#EF6689"),
            row=1,
            col=1,
        )
        fig.add_scatter(
            name=f"{columns_regex(df_ta, 'KCL')[0]}",
            x=df_ta.index,
            y=df_ta[columns_regex(df_ta, "KCL")[0]].values,
            opacity=kc_opacity,
            mode="lines",
            line=dict(width=0.3, color="#EF6689"),
            fill="tonexty",
            fillcolor=fillcolor,
            row=1,
            col=1,
        )
        fig.add_annotation(
            xref="paper",
            yref="paper",
            text=(
                f"<b>KC{self.params['kc'].get_argument_values('length') or ''},"
                f"{self.params['kc'].get_argument_values('scalar') or ''}</b>"
            ),
            x=0,
            xanchor="left",
            yshift=-inchart_index * 18,
            xshift=-60,
            y=0.98,
            font_size=14,
            font_color="#B47DA0",
            opacity=0.9,
        )

        return fig, inchart_index + 1
