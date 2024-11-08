from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag import DAG
from ...models.dag_collection import DAGCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DAG,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    update_mask: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    dag_id_pattern: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_update_mask: Union[Unset, List[str]] = UNSET
    if not isinstance(update_mask, Unset):
        json_update_mask = update_mask

    params["update_mask"] = json_update_mask

    params["only_active"] = only_active

    params["dag_id_pattern"] = dag_id_pattern

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": "/dags",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: DAG,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    update_mask: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    dag_id_pattern: str,
) -> Response[Union[Any, DAGCollection]]:
    """Update DAGs

     Update DAGs of a given dag_id_pattern using UpdateMask.
    This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
    *New in version 2.3.0*

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        tags (Union[Unset, List[str]]):
        update_mask (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        dag_id_pattern (str):
        body (DAG): DAG

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGCollection]]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        offset=offset,
        tags=tags,
        update_mask=update_mask,
        only_active=only_active,
        dag_id_pattern=dag_id_pattern,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DAG,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    update_mask: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    dag_id_pattern: str,
) -> Optional[Union[Any, DAGCollection]]:
    """Update DAGs

     Update DAGs of a given dag_id_pattern using UpdateMask.
    This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
    *New in version 2.3.0*

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        tags (Union[Unset, List[str]]):
        update_mask (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        dag_id_pattern (str):
        body (DAG): DAG

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGCollection]
    """

    return sync_detailed(
        client=client,
        body=body,
        limit=limit,
        offset=offset,
        tags=tags,
        update_mask=update_mask,
        only_active=only_active,
        dag_id_pattern=dag_id_pattern,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DAG,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    update_mask: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    dag_id_pattern: str,
) -> Response[Union[Any, DAGCollection]]:
    """Update DAGs

     Update DAGs of a given dag_id_pattern using UpdateMask.
    This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
    *New in version 2.3.0*

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        tags (Union[Unset, List[str]]):
        update_mask (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        dag_id_pattern (str):
        body (DAG): DAG

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGCollection]]
    """

    kwargs = _get_kwargs(
        body=body,
        limit=limit,
        offset=offset,
        tags=tags,
        update_mask=update_mask,
        only_active=only_active,
        dag_id_pattern=dag_id_pattern,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DAG,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    tags: Union[Unset, List[str]] = UNSET,
    update_mask: Union[Unset, List[str]] = UNSET,
    only_active: Union[Unset, bool] = True,
    dag_id_pattern: str,
) -> Optional[Union[Any, DAGCollection]]:
    """Update DAGs

     Update DAGs of a given dag_id_pattern using UpdateMask.
    This endpoint allows specifying `~` as the dag_id_pattern to update all DAGs.
    *New in version 2.3.0*

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        tags (Union[Unset, List[str]]):
        update_mask (Union[Unset, List[str]]):
        only_active (Union[Unset, bool]):  Default: True.
        dag_id_pattern (str):
        body (DAG): DAG

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            limit=limit,
            offset=offset,
            tags=tags,
            update_mask=update_mask,
            only_active=only_active,
            dag_id_pattern=dag_id_pattern,
        )
    ).parsed
