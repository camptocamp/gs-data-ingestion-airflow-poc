from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_task_instance_note import SetTaskInstanceNote
from ...models.task_instance import TaskInstance
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    body: SetTaskInstanceNote,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/setNote",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskInstance]]:
    if response.status_code == 200:
        response_200 = TaskInstance.from_dict(response.json())

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
) -> Response[Union[Any, TaskInstance]]:
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
    body: SetTaskInstanceNote,
) -> Response[Union[Any, TaskInstance]]:
    """Update the TaskInstance note.

     Update the manual user note of a non-mapped Task Instance.

    *New in version 2.5.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (SetTaskInstanceNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstance]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
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
    body: SetTaskInstanceNote,
) -> Optional[Union[Any, TaskInstance]]:
    """Update the TaskInstance note.

     Update the manual user note of a non-mapped Task Instance.

    *New in version 2.5.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (SetTaskInstanceNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstance]
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTaskInstanceNote,
) -> Response[Union[Any, TaskInstance]]:
    """Update the TaskInstance note.

     Update the manual user note of a non-mapped Task Instance.

    *New in version 2.5.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (SetTaskInstanceNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstance]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTaskInstanceNote,
) -> Optional[Union[Any, TaskInstance]]:
    """Update the TaskInstance note.

     Update the manual user note of a non-mapped Task Instance.

    *New in version 2.5.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        body (SetTaskInstanceNote):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstance]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
