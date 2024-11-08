import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_instance_collection import TaskInstanceCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
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
    duration_gte: Union[Unset, float] = UNSET,
    duration_lte: Union[Unset, float] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    pool: Union[Unset, List[str]] = UNSET,
    queue: Union[Unset, List[str]] = UNSET,
    executor: Union[Unset, List[str]] = UNSET,
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

    params["duration_gte"] = duration_gte

    params["duration_lte"] = duration_lte

    json_state: Union[Unset, List[str]] = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    json_pool: Union[Unset, List[str]] = UNSET
    if not isinstance(pool, Unset):
        json_pool = pool

    params["pool"] = json_pool

    json_queue: Union[Unset, List[str]] = UNSET
    if not isinstance(queue, Unset):
        json_queue = queue

    params["queue"] = json_queue

    json_executor: Union[Unset, List[str]] = UNSET
    if not isinstance(executor, Unset):
        json_executor = executor

    params["executor"] = json_executor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskInstanceCollection]]:
    if response.status_code == 200:
        response_200 = TaskInstanceCollection.from_dict(response.json())

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
) -> Response[Union[Any, TaskInstanceCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
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
    duration_gte: Union[Unset, float] = UNSET,
    duration_lte: Union[Unset, float] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    pool: Union[Unset, List[str]] = UNSET,
    queue: Union[Unset, List[str]] = UNSET,
    executor: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, TaskInstanceCollection]]:
    """List task instances

     This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and
    DAG runs.

    Args:
        dag_id (str):
        dag_run_id (str):
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
        duration_gte (Union[Unset, float]):
        duration_lte (Union[Unset, float]):
        state (Union[Unset, List[str]]):
        pool (Union[Unset, List[str]]):
        queue (Union[Unset, List[str]]):
        executor (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
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
        duration_gte=duration_gte,
        duration_lte=duration_lte,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
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
    duration_gte: Union[Unset, float] = UNSET,
    duration_lte: Union[Unset, float] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    pool: Union[Unset, List[str]] = UNSET,
    queue: Union[Unset, List[str]] = UNSET,
    executor: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, TaskInstanceCollection]]:
    """List task instances

     This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and
    DAG runs.

    Args:
        dag_id (str):
        dag_run_id (str):
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
        duration_gte (Union[Unset, float]):
        duration_lte (Union[Unset, float]):
        state (Union[Unset, List[str]]):
        pool (Union[Unset, List[str]]):
        queue (Union[Unset, List[str]]):
        executor (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceCollection]
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
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
        duration_gte=duration_gte,
        duration_lte=duration_lte,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
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
    duration_gte: Union[Unset, float] = UNSET,
    duration_lte: Union[Unset, float] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    pool: Union[Unset, List[str]] = UNSET,
    queue: Union[Unset, List[str]] = UNSET,
    executor: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, TaskInstanceCollection]]:
    """List task instances

     This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and
    DAG runs.

    Args:
        dag_id (str):
        dag_run_id (str):
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
        duration_gte (Union[Unset, float]):
        duration_lte (Union[Unset, float]):
        state (Union[Unset, List[str]]):
        pool (Union[Unset, List[str]]):
        queue (Union[Unset, List[str]]):
        executor (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
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
        duration_gte=duration_gte,
        duration_lte=duration_lte,
        state=state,
        pool=pool,
        queue=queue,
        executor=executor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
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
    duration_gte: Union[Unset, float] = UNSET,
    duration_lte: Union[Unset, float] = UNSET,
    state: Union[Unset, List[str]] = UNSET,
    pool: Union[Unset, List[str]] = UNSET,
    queue: Union[Unset, List[str]] = UNSET,
    executor: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, TaskInstanceCollection]]:
    """List task instances

     This endpoint allows specifying `~` as the dag_id, dag_run_id to retrieve DAG runs for all DAGs and
    DAG runs.

    Args:
        dag_id (str):
        dag_run_id (str):
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
        duration_gte (Union[Unset, float]):
        duration_lte (Union[Unset, float]):
        state (Union[Unset, List[str]]):
        pool (Union[Unset, List[str]]):
        queue (Union[Unset, List[str]]):
        executor (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceCollection]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
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
            duration_gte=duration_gte,
            duration_lte=duration_lte,
            state=state,
            pool=pool,
            queue=queue,
            executor=executor,
        )
    ).parsed
