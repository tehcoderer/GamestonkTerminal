import logging
import os
import time
from functools import reduce
from multiprocessing import Pool

import df2img
import disnake
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

import bots.config_discordbot as cfg
from bots import helpers
from bots.config_discordbot import gst_imgur
from bots.menus.menu import Menu
from gamestonk_terminal.decorators import log_start_end
from gamestonk_terminal.stocks.options import op_helpers, yfinance_model
from gamestonk_terminal.stocks.options.barchart_model import get_options_info

logger = logging.getLogger(__name__)


def unpack(tup):

    return reduce(np.append, tup)


column_map = {"openInterest": "oi", "volume": "vol", "impliedVolatility": "iv"}
columns = [
    "strike",
    "bid",
    "ask",
    "volume",
    "openInterest",
    "impliedVolatility",
]
titles, embeds, embeds_img, choices = [], [], [], []
plt_link = ""
i2 = 0
puts_page = 3


@log_start_end(log=logger)
def options_run(
    ticker,
    url,
    expiry,
    dates,
    df_bcinfo,
    calls,
    puts,
    df_opt,
    current_price,
    min_strike,
    max_strike,
    min_strike2,
    max_strike2,
    max_pain,
):
    """Options Overview"""
    puts_page = 3
    iv = ""
    fig = go.Figure()

    dmax = df_opt[["OI_call", "OI_put"]].values.max()
    dmin = df_opt[["OI_call", "OI_put"]].values.min()
    fig.add_trace(
        go.Scatter(
            x=df_opt.index,
            y=df_opt["OI_call"],
            name="Calls",
            mode="lines+markers",
            line=dict(color="green", width=3),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df_opt.index,
            y=df_opt["OI_put"],
            name="Puts",
            mode="lines+markers",
            line=dict(color="red", width=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[current_price, current_price],
            y=[dmin, dmax],
            mode="lines",
            line=dict(color="gold", width=2),
            name="Current Price",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[max_pain, max_pain],
            y=[dmin, dmax],
            mode="lines",
            line=dict(color="grey", width=3, dash="dash"),
            name=f"Max Pain: {max_pain}",
        )
    )
    fig.update_xaxes(
        range=[min_strike, max_strike],
        constrain="domain",
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=60, b=20),
        template=cfg.PLT_SCAT_STYLE_TEMPLATE,
        title=f"Open Interest for {ticker.upper()} expiring {expiry}",
        title_x=0.5,
        legend_title="",
        xaxis_title="Strike",
        yaxis_title="Open Interest (1k)",
        xaxis=dict(
            rangeslider=dict(visible=False),
        ),
        font=cfg.PLT_FONT,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        dragmode="pan",
    )
    config = dict({"scrollZoom": True})

    plt_link = ""
    if cfg.INTERACTIVE:
        html_ran = helpers.uuid_get()
        fig.write_html(f"in/oi_{html_ran}.html", config=config)
        plt_link = f"[Interactive]({cfg.INTERACTIVE_URL}/oi_{html_ran}.html)"

    fig.update_layout(
        width=800,
        height=500,
    )
    imagefile = "opt-oi.png"
    imagefile = helpers.image_border(imagefile, fig=fig)

    if cfg.IMAGES_URL:
        image_link_oi = cfg.IMAGES_URL + imagefile
    else:
        imagefile_save = cfg.IMG_DIR + imagefile
        uploaded_image_oi = gst_imgur.upload_image(imagefile_save, title="something")
        image_link_oi = uploaded_image_oi.link
        os.remove(imagefile_save)

    df_bcinfo = df_bcinfo

    calls_df = calls[columns].rename(columns=column_map)
    calls_df = calls_df[calls_df["strike"] >= min_strike2]
    calls_df = calls_df[calls_df["strike"] <= max_strike2]
    calls_df["iv"] = pd.to_numeric(calls_df["iv"].astype(float))

    formats = {"iv": "{:.2f}"}
    for col, f in formats.items():
        calls_df[col] = calls_df[col].map(
            lambda x: f.format(x)  # pylint: disable=W0640
        )

    calls_df = calls_df.fillna("")
    calls_df.set_index("strike", inplace=True)

    if "^" not in ticker:
        if "-" in df_bcinfo.iloc[0, 1]:
            iv = f"```diff\n-             {df_bcinfo.iloc[0, 1]}\n```"
        else:
            iv = f"```yaml\n              {df_bcinfo.iloc[0, 1]}\n```"

    pfix, sfix = f"{ticker.upper()} ", f" expiring {expiry}"
    if expiry == dates[0]:
        pfix = f"{ticker.upper()} Weekly "
        sfix = ""

    titles.append(
        f"{ticker.upper()} Overview",
    )
    titles.append(
        f"{pfix}Open Interest{sfix}",
    )
    embeds.append(
        disnake.Embed(
            title=f"{ticker.upper()} Overview",
            color=cfg.COLOR,
        ),
    )
    embeds.append(
        disnake.Embed(
            title=f"{pfix}Open Interest{sfix}",
            description=plt_link,
            colour=cfg.COLOR,
        ),
    )
    choices.append(
        disnake.SelectOption(label=f"{ticker.upper()} Overview", value="0", emoji="🟢"),
    )
    choices.append(
        disnake.SelectOption(label=f"{pfix}Open Interest{sfix}", value="1", emoji="🟢"),
    )

    i, i2, end = 0, 0, 20
    df_calls = []
    dindex = len(calls_df.index)
    while i <= dindex:
        df_calls = calls_df.iloc[i:end]
        df_calls.append(df_calls)
        figc = df2img.plot_dataframe(
            df_calls,
            fig_size=(1000, (40 + (40 * 20))),
            col_width=[3, 3, 3, 3],
            tbl_header=cfg.PLT_TBL_HEADER,
            tbl_cells=cfg.PLT_TBL_CELLS,
            font=cfg.PLT_TBL_FONT,
            paper_bgcolor="rgba(0, 0, 0, 0)",
        )
        imagefile = "opt-calls.png"
        imagefile = helpers.save_image(imagefile, figc)

        if cfg.IMAGES_URL:
            image_link = cfg.IMAGES_URL + imagefile
        else:
            imagefile_save = cfg.IMG_DIR + imagefile
            uploaded_image = gst_imgur.upload_image(imagefile_save, title="something")
            image_link = uploaded_image.link
            os.remove(imagefile_save)

        embeds_img.append(
            f"{image_link}",
        )
        titles.append(
            f"{pfix}Calls{sfix}",
        )
        embeds.append(
            disnake.Embed(
                title=f"{pfix}Calls{sfix}",
                colour=cfg.COLOR,
            ),
        )
        i2 += 1
        i += 20
        end += 20

    # Add Calls page field
    i, page = 2, 0
    i3 = i2 + 2
    choices.append(
        disnake.SelectOption(label="Calls Page 1", value="2", emoji="🟢"),
    )
    for i in range(2, i3):
        page += 1
        puts_page += 1

        embeds[i].add_field(name=f"Calls Page {page}", value="_ _", inline=True)

    puts_df = puts[columns].rename(columns=column_map)

    puts_df = puts_df[puts_df["strike"] >= min_strike2]
    puts_df = puts_df[puts_df["strike"] <= max_strike2]

    puts_df["iv"] = pd.to_numeric(puts_df["iv"].astype(float))

    formats = {"iv": "{:.2f}"}
    for col, f in formats.items():
        puts_df[col] = puts_df[col].map(lambda x: f.format(x))  # pylint: disable=W0640

    puts_df = puts_df.fillna("")
    puts_df.set_index("strike", inplace=True)

    pfix, sfix = f"{ticker.upper()} ", f" expiring {expiry}"
    if expiry == dates[0]:
        pfix = f"{ticker.upper()} Weekly "
        sfix = ""

    # Puts Pages
    i, end = 0, 20
    df_puts = []

    dindex = len(puts_df.index)
    while i <= dindex:
        df_puts = puts_df.iloc[i:end]
        df_puts.append(df_puts)
        figp = df2img.plot_dataframe(
            df_puts,
            fig_size=(1000, (40 + (40 * 20))),
            col_width=[3, 3, 3, 3],
            tbl_header=cfg.PLT_TBL_HEADER,
            tbl_cells=cfg.PLT_TBL_CELLS,
            font=cfg.PLT_TBL_FONT,
            paper_bgcolor="rgba(0, 0, 0, 0)",
        )
        imagefile = "opt-puts.png"
        imagefile = helpers.save_image(imagefile, figp)

        if cfg.IMAGES_URL:
            image_link = cfg.IMAGES_URL + imagefile
        else:
            imagefile_save = cfg.IMG_DIR + imagefile
            uploaded_image = gst_imgur.upload_image(imagefile_save, title="something")
            image_link = uploaded_image.link
            os.remove(imagefile_save)

        embeds_img.append(
            f"{image_link}",
        )
        titles.append(
            f"{pfix}Puts{sfix}",
        )
        embeds.append(
            disnake.Embed(
                title=f"{pfix}Puts{sfix}",
                colour=cfg.COLOR,
            ),
        )
        i2 += 1
        i += 20
        end += 20

    # Add Puts page field
    i, page = 0, 0
    puts_page -= 1
    i2 += 2
    choices.append(
        disnake.SelectOption(label="Puts Page 1", value=f"{puts_page}", emoji="🟢"),
    )
    for i in range(puts_page, i2):
        page += 1
        embeds[i].add_field(name=f"Puts Page {page}", value="_ _", inline=True)

    # Author/Footer
    for i in range(0, i2):
        embeds[i].set_author(
            name=cfg.AUTHOR_NAME,
            url=cfg.AUTHOR_URL,
            icon_url=cfg.AUTHOR_ICON_URL,
        )
        embeds[i].set_footer(
            text=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )

    # Set images to Pages
    i = 0
    img_i = 0
    embeds[1].set_image(url=image_link_oi)
    for i in range(2, i2):
        embeds[i].set_image(url=embeds_img[img_i])
        img_i += 1
        i += 1

    if url:
        embeds[0].set_thumbnail(url=f"{url}")
    else:
        embeds[0].set_thumbnail(url=cfg.AUTHOR_ICON_URL)
    df_bcinfo = df_bcinfo
    # Overview Section
    if "^" not in ticker:
        embeds[0].add_field(name=f"{df_bcinfo.iloc[0, 0]}", value=iv, inline=False)

        embeds[0].add_field(
            name=f"•{df_bcinfo.iloc[1, 0]}",
            value=f"```css\n{df_bcinfo.iloc[1, 1]}\n```",
            inline=True,
        )
        for N in range(2, 6):
            embeds[0].add_field(
                name=f"_ _ _ _ _ _ _ _ _ _ •{df_bcinfo.iloc[N, 0]}",
                value=f"```css\n{df_bcinfo.iloc[N, 1]}\n```",
                inline=True,
            )

        embeds[0].add_field(name="_ _", value="_ _", inline=False)
        for N in range(6, 8):
            embeds[0].add_field(
                name=f"_ _ _ _ _ _ _ _ _ _ •{df_bcinfo.iloc[N, 0]}",
                value=f"```css\n{df_bcinfo.iloc[N, 1]}\n```",
                inline=True,
            )

        embeds[0].add_field(name="_ _", value="_ _", inline=False)
        for N in range(8, 10):
            embeds[0].add_field(
                name=f"_ _ _ _ _ _ _ _ _ _ •{df_bcinfo.iloc[N, 0]}",
                value=f"```css\n{df_bcinfo.iloc[N, 1]}\n```",
                inline=True,
            )

        embeds[0].add_field(name="_ _", value="_ _", inline=False)
        for N in range(10, 12):
            embeds[0].add_field(
                name=f"_ _ _ _ _ _ _ _ _ _ •{df_bcinfo.iloc[N, 0]}",
                value=f"```css\n{df_bcinfo.iloc[N, 1]}\n```",
                inline=True,
            )

        embeds[0].set_footer(text=f"Page 1 of {len(embeds)}")

    return titles, embeds, choices, embeds_img


def options_data(
    ticker: str = None,
    expiry: str = None,
    min_sp: float = None,
    max_sp: float = None,
):

    # Debug
    if cfg.DEBUG:
        logger.debug("opt overview %s %s %s %s", ticker, expiry, min_sp, max_sp)

    # Check for argument
    if ticker is None:
        raise Exception("Stock ticker is required")

    df_bcinfo = ""
    # Get options info/dates, Look for logo_url
    if "^" not in ticker:
        df_bcinfo = get_options_info(ticker)  # Barchart Options IV Overview

    dates = yfinance_model.option_expirations(ticker)  # Expiration dates
    tup = f"{ticker.upper()}"
    url = yf.Ticker(tup).info["logo_url"]
    url += "?raw=true" if url else ""

    if not dates:
        raise Exception("Stock ticker is invalid")

    options = yfinance_model.get_option_chain(ticker, str(expiry))
    calls = options.calls.fillna(0)
    puts = options.puts.fillna(0)

    current_price = yfinance_model.get_price(ticker)

    min_strike2 = np.percentile(calls["strike"], 1)
    max_strike2 = np.percentile(calls["strike"], 100)
    min_strike = 0.75 * current_price
    max_strike = 1.95 * current_price

    if len(calls) > 40:
        min_strike = 0.75 * current_price
        max_strike = 1.25 * current_price

    if min_sp:
        min_strike = min_sp
        min_strike2 = min_sp
    if max_sp:
        max_strike = max_sp
        max_strike2 = max_sp
        if min_sp > max_sp:  # type: ignore
            min_sp, max_sp = max_strike2, min_strike2

    call_oi = calls.set_index("strike")["openInterest"] / 1000
    put_oi = puts.set_index("strike")["openInterest"] / 1000

    df_opt = pd.merge(call_oi, put_oi, left_index=True, right_index=True)
    df_opt = df_opt.rename(
        columns={"openInterest_x": "OI_call", "openInterest_y": "OI_put"}
    )

    max_pain = op_helpers.calculate_max_pain(df_opt)
    data = [
        ticker,
        url,
        expiry,
        dates,
        df_bcinfo,
        calls,
        puts,
        df_opt,
        current_price,
        min_strike,
        max_strike,
        min_strike2,
        max_strike2,
        max_pain,
    ]
    return data


print(__name__)


def run(
    ticker: str = None,
    expiry: str = None,
    min_sp: float = None,
    max_sp: float = None,
):

    print("start")
    cpus = os.cpu_count()
    data = options_data(ticker, expiry, min_sp, max_sp)
    with Pool(processes=cpus) as p:
        time.sleep(1)
        timer0 = time.perf_counter()
        titles, embeds, choices, embeds_img = zip(
            *p.starmap(options_run, [(*data,)], chunksize=1)
        )
        timer1 = time.perf_counter()

        deltat = timer1 - timer0

        print(f"\nGenerated in {deltat:.1f} seconds")

    return unpack(titles), unpack(embeds), unpack(choices), unpack(embeds_img)


def overview_command(
    ticker: str = None,
    expiry: str = None,
    min_sp: float = None,
    max_sp: float = None,
):
    timer0 = time.perf_counter()
    titles, embeds, choices, embeds_img = run(ticker, expiry, min_sp, max_sp)
    timer1 = time.perf_counter()
    deltat = timer1 - timer0
    print(f"\nGenerated2 in {deltat:.1f} seconds")
    return {
        "view": Menu,
        "titles": titles,
        "embed": embeds,
        "choices": choices,
        "embeds_img": embeds_img,
    }
