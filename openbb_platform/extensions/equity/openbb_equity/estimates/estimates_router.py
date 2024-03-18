"""Estimates Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/estimates")

# pylint: disable=unused-argument


@router.command(
    model="PriceTarget",
    examples=[
        APIEx(parameters={"provider": "benzinga"}),
        APIEx(
            description="Get price targets for Microsoft using 'benzinga' as provider.",
            parameters={
                "start_date": "2020-01-01",
                "end_date": "2024-02-16",
                "limit": 10,
                "symbol": "msft",
                "provider": "benzinga",
                "action": "downgrades",
            },
        ),
    ],
)
async def price_target(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get analyst price targets by company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="AnalystEstimates",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
    ],
)
async def historical(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get historical analyst estimates for earnings and revenue."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="PriceTargetConsensus",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(parameters={"symbol": "AAPL,MSFT", "provider": "yfinance"}),
    ],
)
async def consensus(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Get consensus price target and recommendation."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="AnalystSearch",
    examples=[
        APIEx(parameters={"provider": "benzinga"}),
        APIEx(parameters={"firm_name": "Wedbush", "provider": "benzinga"}),
    ],
)
async def analyst_search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject:
    """Search for specific analysts and get their forecast track record."""
    return await OBBject.from_query(Query(**locals()))
