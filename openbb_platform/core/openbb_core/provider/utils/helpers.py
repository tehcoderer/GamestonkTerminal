"""Provider helpers."""

import asyncio
import re
from datetime import datetime
from difflib import SequenceMatcher
from functools import partial
from inspect import iscoroutinefunction
from typing import Awaitable, Callable, List, Literal, Optional, TypeVar, Union, cast

import requests
from anyio import start_blocking_portal
from typing_extensions import ParamSpec

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.utils.client import (
    ClientResponse,
    ClientSession,
    get_user_agent,
)

T = TypeVar("T")
P = ParamSpec("P")


def check_item(item: str, allowed: List[str], threshold: float = 0.75) -> None:
    """Check if an item is in a list of allowed items and raise an error if not.

    Parameters
    ----------
    item : str
        The item to check.
    allowed : List[str]
        The list of allowed items.
    threshold : float, optional
        The similarity threshold for the error message, by default 0.75

    Raises
    ------
    ValueError
        If the item is not in the allowed list.
    """
    if item not in allowed:
        similarities = map(
            lambda c: (c, SequenceMatcher(None, item, c).ratio()), allowed
        )
        similar, score = max(similarities, key=lambda x: x[1])
        if score > threshold:
            raise ValueError(f"'{item}' is not available. Did you mean '{similar}'?")
        raise ValueError(f"'{item}' is not available.")


def get_querystring(items: dict, exclude: List[str]) -> str:
    """Turn a dictionary into a querystring, excluding the keys in the exclude list.

    Parameters
    ----------
    items: dict
        The dictionary to be turned into a querystring.

    exclude: List[str]
        The keys to be excluded from the querystring.

    Returns
    -------
    str
        The querystring.
    """
    for key in exclude:
        items.pop(key, None)

    query_items = []
    for key, value in items.items():
        if value is None:
            continue
        if isinstance(value, list):
            for item in value:
                query_items.append(f"{key}={item}")
        else:
            query_items.append(f"{key}={value}")

    querystring = "&".join(query_items)

    return f"{querystring}" if querystring else ""


async def amake_request(
    url: str,
    method: Literal["GET", "POST"] = "GET",
    timeout: int = 10,
    response_callback: Optional[
        Callable[[ClientResponse, ClientSession], Awaitable[Union[dict, List[dict]]]]
    ] = None,
    **kwargs,
) -> Union[dict, List[dict]]:
    """
    Abstract helper to make requests from a url with potential headers and params.

    Parameters
    ----------
    url : str
        Url to make the request to
    method : str, optional
        HTTP method to use.  Can be "GET" or "POST", by default "GET"
    timeout : int, optional
        Timeout in seconds, by default 10.  Can be overwritten by user setting, request_timeout
    response_callback : Callable[[ClientResponse, ClientSession], Awaitable[Union[dict, List[dict]]]], optional
        Async callback with response and session as arguments that returns the json, by default None
    session : ClientSession, optional
        Custom session to use for requests, by default None


    Returns
    -------
    Union[dict, List[dict]]
        Response json
    """
    if method.upper() not in ["GET", "POST"]:
        raise ValueError("Method must be GET or POST")

    kwargs["timeout"] = kwargs.pop("preferences", {}).get("request_timeout", timeout)

    response_callback = response_callback or (
        lambda r, _: asyncio.ensure_future(r.json())
    )

    with_session = kwargs.pop("with_session", "session" in kwargs)
    session: ClientSession = kwargs.pop("session", ClientSession())

    try:
        response = await session.request(method, url, **kwargs)
        return await response_callback(response, session)
    finally:
        if not with_session:
            await session.close()


async def amake_requests(
    urls: Union[str, List[str]],
    response_callback: Optional[
        Callable[[ClientResponse, ClientSession], Awaitable[Union[dict, List[dict]]]]
    ] = None,
    **kwargs,
):
    """Make multiple requests asynchronously.

    Parameters
    ----------
    urls : Union[str, List[str]]
        List of urls to make requests to
    method : Literal["GET", "POST"], optional
        HTTP method to use.  Can be "GET" or "POST", by default "GET"
    timeout : int, optional
        Timeout in seconds, by default 10.  Can be overwritten by user setting, request_timeout
    response_callback : Callable[[ClientResponse, ClientSession], Awaitable[Union[dict, List[dict]]]], optional
        Async callback with response and session as arguments that returns the json, by default None
    session : ClientSession, optional
        Custom session to use for requests, by default None

    Returns
    -------
    Union[dict, List[dict]]
        Response json
    """
    session: ClientSession = kwargs.pop("session", ClientSession())
    kwargs["response_callback"] = response_callback

    urls = urls if isinstance(urls, list) else [urls]

    try:
        results = []

        for result in await asyncio.gather(
            *[amake_request(url, session=session, **kwargs) for url in urls],
            return_exceptions=True,
        ):
            is_exception = isinstance(result, Exception)

            if is_exception and kwargs.get("raise_for_status", False):
                raise result

            if is_exception or not result:
                continue

            results.extend(  # type: ignore
                result if isinstance(result, list) else [result]
            )

        return results

    finally:
        await session.close()


def make_request(
    url: str, method: str = "GET", timeout: int = 10, **kwargs
) -> requests.Response:
    """Abstract helper to make requests from a url with potential headers and params.

    Parameters
    ----------
    url : str
        Url to make the request to
    method : str, optional
        HTTP method to use.  Can be "GET" or "POST", by default "GET"
    timeout : int, optional
        Timeout in seconds, by default 10.  Can be overwritten by user setting, request_timeout

    Returns
    -------
    requests.Response
        Request response object

    Raises
    ------
    ValueError
        If invalid method is passed
    """
    # We want to add a user agent to the request, so check if there are any headers
    # If there are headers, check if there is a user agent, if not add one.
    # Some requests seem to work only with a specific user agent, so we want to be able to override it.
    headers = kwargs.pop("headers", {})
    preferences = kwargs.pop("preferences", None)
    if preferences and "request_timeout" in preferences:
        timeout = preferences["request_timeout"] or timeout

    if "User-Agent" not in headers:
        headers["User-Agent"] = get_user_agent()

    # Allow a custom session for caching, if desired
    _session = kwargs.pop("session", None) or requests

    if method.upper() == "GET":
        return _session.get(
            url,
            headers=headers,
            timeout=timeout,
            **kwargs,
        )
    if method.upper() == "POST":
        return _session.post(
            url,
            headers=headers,
            timeout=timeout,
            **kwargs,
        )
    raise ValueError("Method must be GET or POST")


def to_snake_case(string: str) -> str:
    """Convert a string to snake case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return (
        re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
        .lower()
        .replace(" ", "_")
        .replace("__", "_")
    )


async def maybe_coroutine(
    func: Callable[P, Union[T, Awaitable[T]]], /, *args: P.args, **kwargs: P.kwargs
) -> T:
    """Check if a function is a coroutine and run it accordingly."""
    if not iscoroutinefunction(func):
        return cast(T, func(*args, **kwargs))

    return await func(*args, **kwargs)


def run_async(
    func: Callable[P, Awaitable[T]], /, *args: P.args, **kwargs: P.kwargs
) -> T:
    """Run a coroutine function in a blocking context."""
    if not iscoroutinefunction(func):
        return cast(T, func(*args, **kwargs))

    with start_blocking_portal() as portal:
        try:
            return portal.call(partial(func, *args, **kwargs))
        finally:
            portal.call(portal.stop)


def filter_by_dates(
    data: List[Data],
    start_date: datetime,
    end_date: datetime,
) -> List[Data]:
    """Filter data by dates."""
    if not any([start_date, end_date]):
        return data

    return list(
        filter(
            lambda d: start_date <= d.date.date() <= end_date,
            data,
        )
    )
