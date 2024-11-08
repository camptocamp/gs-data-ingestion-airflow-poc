from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dataset_event_collection import DatasetEventCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dataset_id: Union[Unset, int] = UNSET,
    source_dag_id: Union[Unset, str] = UNSET,
    source_task_id: Union[Unset, str] = UNSET,
    source_run_id: Union[Unset, str] = UNSET,
    source_map_index: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params["dataset_id"] = dataset_id

    params["source_dag_id"] = source_dag_id

    params["source_task_id"] = source_task_id

    params["source_run_id"] = source_run_id

    params["source_map_index"] = source_map_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/datasets/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DatasetEventCollection]]:
    if response.status_code == 200:
        response_200 = DatasetEventCollection.from_dict(response.json())

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
) -> Response[Union[Any, DatasetEventCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dataset_id: Union[Unset, int] = UNSET,
    source_dag_id: Union[Unset, str] = UNSET,
    source_task_id: Union[Unset, str] = UNSET,
    source_run_id: Union[Unset, str] = UNSET,
    source_map_index: Union[Unset, int] = UNSET,
) -> Response[Union[Any, DatasetEventCollection]]:
    """Get dataset events

     Get dataset events

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dataset_id (Union[Unset, int]):
        source_dag_id (Union[Unset, str]):
        source_task_id (Union[Unset, str]):
        source_run_id (Union[Unset, str]):
        source_map_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DatasetEventCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dataset_id=dataset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dataset_id: Union[Unset, int] = UNSET,
    source_dag_id: Union[Unset, str] = UNSET,
    source_task_id: Union[Unset, str] = UNSET,
    source_run_id: Union[Unset, str] = UNSET,
    source_map_index: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, DatasetEventCollection]]:
    """Get dataset events

     Get dataset events

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dataset_id (Union[Unset, int]):
        source_dag_id (Union[Unset, str]):
        source_task_id (Union[Unset, str]):
        source_run_id (Union[Unset, str]):
        source_map_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DatasetEventCollection]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dataset_id=dataset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dataset_id: Union[Unset, int] = UNSET,
    source_dag_id: Union[Unset, str] = UNSET,
    source_task_id: Union[Unset, str] = UNSET,
    source_run_id: Union[Unset, str] = UNSET,
    source_map_index: Union[Unset, int] = UNSET,
) -> Response[Union[Any, DatasetEventCollection]]:
    """Get dataset events

     Get dataset events

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dataset_id (Union[Unset, int]):
        source_dag_id (Union[Unset, str]):
        source_task_id (Union[Unset, str]):
        source_run_id (Union[Unset, str]):
        source_map_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DatasetEventCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dataset_id=dataset_id,
        source_dag_id=source_dag_id,
        source_task_id=source_task_id,
        source_run_id=source_run_id,
        source_map_index=source_map_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dataset_id: Union[Unset, int] = UNSET,
    source_dag_id: Union[Unset, str] = UNSET,
    source_task_id: Union[Unset, str] = UNSET,
    source_run_id: Union[Unset, str] = UNSET,
    source_map_index: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, DatasetEventCollection]]:
    """Get dataset events

     Get dataset events

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dataset_id (Union[Unset, int]):
        source_dag_id (Union[Unset, str]):
        source_task_id (Union[Unset, str]):
        source_run_id (Union[Unset, str]):
        source_map_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DatasetEventCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            dataset_id=dataset_id,
            source_dag_id=source_dag_id,
            source_task_id=source_task_id,
            source_run_id=source_run_id,
            source_map_index=source_map_index,
        )
    ).parsed
