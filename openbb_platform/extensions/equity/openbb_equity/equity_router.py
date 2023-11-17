"""Equity Router."""

from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (
    ExtraParams,
    ProviderChoices,
    StandardParams,
)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

from openbb_equity.calendar.calendar_router import router as calendar_router
from openbb_equity.compare.compare_router import router as compare_router
from openbb_equity.darkpool.darkpool_router import router as darkpool_router
from openbb_equity.discovery.discovery_router import router as discovery_router
from openbb_equity.estimates.estimates_router import router as estimates_router
from openbb_equity.fundamental.fundamental_router import router as fundamental_router
from openbb_equity.ownership.ownership_router import router as ownership_router
from openbb_equity.price.price_router import router as price_router
from openbb_equity.shorts.shorts_router import router as shorts_router

router = Router(prefix="")
router.include_router(calendar_router)
router.include_router(compare_router)
router.include_router(estimates_router)
router.include_router(darkpool_router)
router.include_router(discovery_router)
router.include_router(fundamental_router)
router.include_router(ownership_router)
router.include_router(price_router)
router.include_router(shorts_router)

# pylint: disable=import-outside-toplevel, W0613:unused-argument


@router.command(model="EquitySearch")
def search(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Equity Search. Search for a company or stock ticker."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="EquityScreener")
def screener(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Equity Screen. Screen for companies meeting various criteria."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="EquityInfo")
def profile(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Equity Info. Get general price and performance metrics of a stock."""
    return OBBject(results=Query(**locals()).execute())


@router.command(model="MarketSnapshots")
def market_snapshots(
    cc: CommandContext,
    provider_choices: ProviderChoices,
    standard_params: StandardParams,
    extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Get a current, complete, market snapshot."""
    return OBBject(results=Query(**locals()).execute())
