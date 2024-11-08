from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_dag_run import ClearDagRun
from ...models.dag_run import DAGRun
from ...models.task_instance_collection import TaskInstanceCollection
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    *,
    body: ClearDagRun,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}/clear",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["DAGRun", "TaskInstanceCollection"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DAGRun.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = TaskInstanceCollection.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
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
    body: ClearDagRun,
) -> Response[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
    """Clear a DAG run

     Clear a DAG run.

    *New in version 2.4.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (ClearDagRun):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['DAGRun', 'TaskInstanceCollection']]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        body=body,
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
    body: ClearDagRun,
) -> Optional[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
    """Clear a DAG run

     Clear a DAG run.

    *New in version 2.4.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (ClearDagRun):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['DAGRun', 'TaskInstanceCollection']]
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClearDagRun,
) -> Response[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
    """Clear a DAG run

     Clear a DAG run.

    *New in version 2.4.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (ClearDagRun):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['DAGRun', 'TaskInstanceCollection']]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClearDagRun,
) -> Optional[Union[Any, Union["DAGRun", "TaskInstanceCollection"]]]:
    """Clear a DAG run

     Clear a DAG run.

    *New in version 2.4.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (ClearDagRun):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['DAGRun', 'TaskInstanceCollection']]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
            body=body,
        )
    ).parsed
