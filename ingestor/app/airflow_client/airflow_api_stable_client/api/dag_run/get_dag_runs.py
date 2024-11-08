import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run_collection import DAGRunCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET,
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET,
    start_date_gte: Union[Unset, datetime.datetime] = UNSET,
    start_date_lte: Union[Unset, datetime.datetime] = UNSET,
    end_date_gte: Union[Unset, datetime.datetime] = UNSET,
    end_date_lte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lte: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_execution_date_gte: Union[Unset, str] = UNSET
    if not isinstance(execution_date_gte, Unset):
        json_execution_date_gte = execution_date_gte.isoformat()
    params["execution_date_gte"] = json_execution_date_gte

    json_execution_date_lte: Union[Unset, str] = UNSET
    if not isinstance(execution_date_lte, Unset):
        json_execution_date_lte = execution_date_lte.isoformat()
    params["execution_date_lte"] = json_execution_date_lte

    json_start_date_gte: Union[Unset, str] = UNSET
    if not isinstance(start_date_gte, Unset):
        json_start_date_gte = start_date_gte.isoformat()
    params["start_date_gte"] = json_start_date_gte

    json_start_date_lte: Union[Unset, str] = UNSET
    if not isinstance(start_date_lte, Unset):
        json_start_date_lte = start_date_lte.isoformat()
    params["start_date_lte"] = json_start_date_lte

    json_end_date_gte: Union[Unset, str] = UNSET
    if not isinstance(end_date_gte, Unset):
        json_end_date_gte = end_date_gte.isoformat()
    params["end_date_gte"] = json_end_date_gte

    json_end_date_lte: Union[Unset, str] = UNSET
    if not isinstance(end_date_lte, Unset):
        json_end_date_lte = end_date_lte.isoformat()
    params["end_date_lte"] = json_end_date_lte

    json_updated_at_gte: Union[Unset, str] = UNSET
    if not isinstance(updated_at_gte, Unset):
        json_updated_at_gte = updated_at_gte.isoformat()
    params["updated_at_gte"] = json_updated_at_gte

    json_updated_at_lte: Union[Unset, str] = UNSET
    if not isinstance(updated_at_lte, Unset):
        json_updated_at_lte = updated_at_lte.isoformat()
    params["updated_at_lte"] = json_updated_at_lte

    json_state: Union[Unset, List[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params["order_by"] = order_by

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}/dagRuns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DAGRunCollection]]:
    if response.status_code == 200:
        response_200 = DAGRunCollection.from_dict(response.json())

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
) -> Response[Union[Any, DAGRunCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET,
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET,
    start_date_gte: Union[Unset, datetime.datetime] = UNSET,
    start_date_lte: Union[Unset, datetime.datetime] = UNSET,
    end_date_gte: Union[Unset, datetime.datetime] = UNSET,
    end_date_lte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lte: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, DAGRunCollection]]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        execution_date_gte (Union[Unset, datetime.datetime]):
        execution_date_lte (Union[Unset, datetime.datetime]):
        start_date_gte (Union[Unset, datetime.datetime]):
        start_date_lte (Union[Unset, datetime.datetime]):
        end_date_gte (Union[Unset, datetime.datetime]):
        end_date_lte (Union[Unset, datetime.datetime]):
        updated_at_gte (Union[Unset, datetime.datetime]):
        updated_at_lte (Union[Unset, datetime.datetime]):
        state (Union[Unset, List[str]]):
        order_by (Union[Unset, str]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGRunCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET,
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET,
    start_date_gte: Union[Unset, datetime.datetime] = UNSET,
    start_date_lte: Union[Unset, datetime.datetime] = UNSET,
    end_date_gte: Union[Unset, datetime.datetime] = UNSET,
    end_date_lte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lte: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, DAGRunCollection]]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        execution_date_gte (Union[Unset, datetime.datetime]):
        execution_date_lte (Union[Unset, datetime.datetime]):
        start_date_gte (Union[Unset, datetime.datetime]):
        start_date_lte (Union[Unset, datetime.datetime]):
        end_date_gte (Union[Unset, datetime.datetime]):
        end_date_lte (Union[Unset, datetime.datetime]):
        updated_at_gte (Union[Unset, datetime.datetime]):
        updated_at_lte (Union[Unset, datetime.datetime]):
        state (Union[Unset, List[str]]):
        order_by (Union[Unset, str]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGRunCollection]
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET,
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET,
    start_date_gte: Union[Unset, datetime.datetime] = UNSET,
    start_date_lte: Union[Unset, datetime.datetime] = UNSET,
    end_date_gte: Union[Unset, datetime.datetime] = UNSET,
    end_date_lte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lte: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, DAGRunCollection]]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        execution_date_gte (Union[Unset, datetime.datetime]):
        execution_date_lte (Union[Unset, datetime.datetime]):
        start_date_gte (Union[Unset, datetime.datetime]):
        start_date_lte (Union[Unset, datetime.datetime]):
        end_date_gte (Union[Unset, datetime.datetime]):
        end_date_lte (Union[Unset, datetime.datetime]):
        updated_at_gte (Union[Unset, datetime.datetime]):
        updated_at_lte (Union[Unset, datetime.datetime]):
        state (Union[Unset, List[str]]):
        order_by (Union[Unset, str]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGRunCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        limit=limit,
        offset=offset,
        execution_date_gte=execution_date_gte,
        execution_date_lte=execution_date_lte,
        start_date_gte=start_date_gte,
        start_date_lte=start_date_lte,
        end_date_gte=end_date_gte,
        end_date_lte=end_date_lte,
        updated_at_gte=updated_at_gte,
        updated_at_lte=updated_at_lte,
        state=state,
        order_by=order_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    execution_date_gte: Union[Unset, datetime.datetime] = UNSET,
    execution_date_lte: Union[Unset, datetime.datetime] = UNSET,
    start_date_gte: Union[Unset, datetime.datetime] = UNSET,
    start_date_lte: Union[Unset, datetime.datetime] = UNSET,
    end_date_gte: Union[Unset, datetime.datetime] = UNSET,
    end_date_lte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_gte: Union[Unset, datetime.datetime] = UNSET,
    updated_at_lte: Union[Unset, datetime.datetime] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, DAGRunCollection]]:
    """List DAG runs

     This endpoint allows specifying `~` as the dag_id to retrieve DAG runs for all DAGs.

    Args:
        dag_id (str):
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        execution_date_gte (Union[Unset, datetime.datetime]):
        execution_date_lte (Union[Unset, datetime.datetime]):
        start_date_gte (Union[Unset, datetime.datetime]):
        start_date_lte (Union[Unset, datetime.datetime]):
        end_date_gte (Union[Unset, datetime.datetime]):
        end_date_lte (Union[Unset, datetime.datetime]):
        updated_at_gte (Union[Unset, datetime.datetime]):
        updated_at_lte (Union[Unset, datetime.datetime]):
        state (Union[Unset, List[str]]):
        order_by (Union[Unset, str]):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGRunCollection]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            limit=limit,
            offset=offset,
            execution_date_gte=execution_date_gte,
            execution_date_lte=execution_date_lte,
            start_date_gte=start_date_gte,
            start_date_lte=start_date_lte,
            end_date_gte=end_date_gte,
            end_date_lte=end_date_lte,
            updated_at_gte=updated_at_gte,
            updated_at_lte=updated_at_lte,
            state=state,
            order_by=order_by,
            fields=fields,
        )
    ).parsed
