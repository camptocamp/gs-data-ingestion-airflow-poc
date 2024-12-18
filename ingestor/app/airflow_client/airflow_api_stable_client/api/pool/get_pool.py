from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pool import Pool
from ...types import Response


def _get_kwargs(
    pool_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/pools/{pool_name}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Pool]]:
    if response.status_code == 200:
        response_200 = Pool.from_dict(response.json())

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
) -> Response[Union[Any, Pool]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Pool]]:
    """Get a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pool]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Pool]]:
    """Get a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Pool]
    """

    return sync_detailed(
        pool_name=pool_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Pool]]:
    """Get a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pool]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Pool]]:
    """Get a pool

    Args:
        pool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Pool]
    """

    return (
        await asyncio_detailed(
            pool_name=pool_name,
            client=client,
        )
    ).parsed
