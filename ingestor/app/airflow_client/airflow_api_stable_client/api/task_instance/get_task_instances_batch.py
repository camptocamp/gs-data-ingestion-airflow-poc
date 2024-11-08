from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_task_instance_form import ListTaskInstanceForm
from ...models.task_instance_collection import TaskInstanceCollection
from ...types import Response


def _get_kwargs(
    *,
    body: ListTaskInstanceForm,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/dags/~/dagRuns/~/taskInstances/list",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListTaskInstanceForm,
) -> Response[Union[Any, TaskInstanceCollection]]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceCollection]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListTaskInstanceForm,
) -> Optional[Union[Any, TaskInstanceCollection]]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceCollection]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListTaskInstanceForm,
) -> Response[Union[Any, TaskInstanceCollection]]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskInstanceCollection]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ListTaskInstanceForm,
) -> Optional[Union[Any, TaskInstanceCollection]]:
    """List task instances (batch)

     List task instances from all DAGs and DAG runs.
    This endpoint is a POST to allow filtering across a large number of DAG IDs, where as a GET it would
    run in to maximum HTTP request URL length limits.

    Args:
        body (ListTaskInstanceForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskInstanceCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
