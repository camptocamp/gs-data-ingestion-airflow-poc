from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pool import Pool
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pool_name: str,
    *,
    body: Pool,
    update_mask: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_update_mask: Union[Unset, List[str]] = UNSET
    if not isinstance(update_mask, Unset):
        json_update_mask = update_mask

    params["update_mask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/pools/{pool_name}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Pool]]:
    if response.status_code == 200:
        response_200 = Pool.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
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
    body: Pool,
    update_mask: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, Pool]]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (Union[Unset, List[str]]):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pool]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Pool,
    update_mask: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, Pool]]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (Union[Unset, List[str]]):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Pool]
    """

    return sync_detailed(
        pool_name=pool_name,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Pool,
    update_mask: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, Pool]]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (Union[Unset, List[str]]):
        body (Pool): The pool

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Pool]]
    """

    kwargs = _get_kwargs(
        pool_name=pool_name,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pool_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Pool,
    update_mask: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, Pool]]:
    """Update a pool

    Args:
        pool_name (str):
        update_mask (Union[Unset, List[str]]):
        body (Pool): The pool

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
            body=body,
            update_mask=update_mask,
        )
    ).parsed
