from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_warning_collection import DagWarningCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    dag_id: Union[Unset, str] = UNSET,
    warning_type: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["dag_id"] = dag_id

    params["warning_type"] = warning_type

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/dagWarnings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DagWarningCollection]]:
    if response.status_code == 200:
        response_200 = DagWarningCollection.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DagWarningCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_id: Union[Unset, str] = UNSET,
    warning_type: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DagWarningCollection]]:
    """List dag warnings

    Args:
        dag_id (Union[Unset, str]):
        warning_type (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DagWarningCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_id: Union[Unset, str] = UNSET,
    warning_type: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DagWarningCollection]]:
    """List dag warnings

    Args:
        dag_id (Union[Unset, str]):
        warning_type (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DagWarningCollection]
    """

    return sync_detailed(
        client=client,
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_id: Union[Unset, str] = UNSET,
    warning_type: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DagWarningCollection]]:
    """List dag warnings

    Args:
        dag_id (Union[Unset, str]):
        warning_type (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DagWarningCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        warning_type=warning_type,
        limit=limit,
        offset=offset,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_id: Union[Unset, str] = UNSET,
    warning_type: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DagWarningCollection]]:
    """List dag warnings

    Args:
        dag_id (Union[Unset, str]):
        warning_type (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DagWarningCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            dag_id=dag_id,
            warning_type=warning_type,
            limit=limit,
            offset=offset,
            order_by=order_by,
        )
    ).parsed
