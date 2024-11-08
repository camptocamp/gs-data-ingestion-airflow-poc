from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.config import Config
from ...types import Response


def _get_kwargs(
    section: str,
    option: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/config/section/{section}/option/{option}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Config]]:
    if response.status_code == 200:
        response_200 = Config.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Config]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    section: str,
    option: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Config]]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Config]]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    section: str,
    option: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Config]]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Config]
    """

    return sync_detailed(
        section=section,
        option=option,
        client=client,
    ).parsed


async def asyncio_detailed(
    section: str,
    option: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Config]]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Config]]
    """

    kwargs = _get_kwargs(
        section=section,
        option=option,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    section: str,
    option: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Config]]:
    """Get a option from configuration

    Args:
        section (str):
        option (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Config]
    """

    return (
        await asyncio_detailed(
            section=section,
            option=option,
            client=client,
        )
    ).parsed
