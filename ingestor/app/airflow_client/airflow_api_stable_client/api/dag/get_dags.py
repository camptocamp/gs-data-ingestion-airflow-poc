from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_collection import DAGCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    paused: Union[Unset, bool] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
    dag_id_pattern: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params["only_active"] = only_active

    params["paused"] = paused

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["dag_id_pattern"] = dag_id_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/dags",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DAGCollection]]:
    if response.status_code == 200:
        response_200 = DAGCollection.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DAGCollection]]:
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
    tags: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    paused: Union[Unset, bool] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
    dag_id_pattern: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DAGCollection]]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        paused (Union[Unset, bool]):
        fields (Union[Unset, List[str]]):
        dag_id_pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
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
    tags: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    paused: Union[Unset, bool] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
    dag_id_pattern: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DAGCollection]]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        paused (Union[Unset, bool]):
        fields (Union[Unset, List[str]]):
        dag_id_pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGCollection]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    paused: Union[Unset, bool] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
    dag_id_pattern: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DAGCollection]]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        paused (Union[Unset, bool]):
        fields (Union[Unset, List[str]]):
        dag_id_pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        tags=tags,
        only_active=only_active,
        paused=paused,
        fields=fields,
        dag_id_pattern=dag_id_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    paused: Union[Unset, bool] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
    dag_id_pattern: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DAGCollection]]:
    """List DAGs

     List DAGs in the database.
    `dag_id_pattern` can be set to match dags of a specific pattern

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        paused (Union[Unset, bool]):
        fields (Union[Unset, List[str]]):
        dag_id_pattern (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            tags=tags,
            only_active=only_active,
            paused=paused,
            fields=fields,
            dag_id_pattern=dag_id_pattern,
        )
    ).parsed
