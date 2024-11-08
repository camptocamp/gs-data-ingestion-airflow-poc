from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_instance_dependency_collection import TaskInstanceDependencyCollection
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/dependencies",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskInstanceDependencyCollection]]:
    if response.status_code == 200:
        response_200 = TaskInstanceDependencyCollection.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, TaskInstanceDependencyCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, TaskInstanceDependencyCollection]]:
    """Get task dependencies blocking task from getting scheduled.

     Get task dependencies blocking task from getting scheduled.

    *New in version 2.10.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceDependencyCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, TaskInstanceDependencyCollection]]:
    """Get task dependencies blocking task from getting scheduled.

     Get task dependencies blocking task from getting scheduled.

    *New in version 2.10.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceDependencyCollection]
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, TaskInstanceDependencyCollection]]:
    """Get task dependencies blocking task from getting scheduled.

     Get task dependencies blocking task from getting scheduled.

    *New in version 2.10.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceDependencyCollection]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, TaskInstanceDependencyCollection]]:
    """Get task dependencies blocking task from getting scheduled.

     Get task dependencies blocking task from getting scheduled.

    *New in version 2.10.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceDependencyCollection]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
        )
    ).parsed
