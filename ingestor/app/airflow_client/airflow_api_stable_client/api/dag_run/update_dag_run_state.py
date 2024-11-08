from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_run import DAGRun
from ...models.update_dag_run_state import UpdateDagRunState
from ...types import Response


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    *,
    body: UpdateDagRunState,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DAGRun]]:
    if response.status_code == 200:
        response_200 = DAGRun.from_dict(response.json())

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
) -> Response[Union[Any, DAGRun]]:
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
    body: UpdateDagRunState,
) -> Response[Union[Any, DAGRun]]:
    """Modify a DAG run

     Modify a DAG run.

    *New in version 2.2.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (UpdateDagRunState): Modify the state of a DAG run.

            *New in version 2.2.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGRun]]
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
    body: UpdateDagRunState,
) -> Optional[Union[Any, DAGRun]]:
    """Modify a DAG run

     Modify a DAG run.

    *New in version 2.2.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (UpdateDagRunState): Modify the state of a DAG run.

            *New in version 2.2.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGRun]
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
    body: UpdateDagRunState,
) -> Response[Union[Any, DAGRun]]:
    """Modify a DAG run

     Modify a DAG run.

    *New in version 2.2.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (UpdateDagRunState): Modify the state of a DAG run.

            *New in version 2.2.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAGRun]]
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
    body: UpdateDagRunState,
) -> Optional[Union[Any, DAGRun]]:
    """Modify a DAG run

     Modify a DAG run.

    *New in version 2.2.0*

    Args:
        dag_id (str):
        dag_run_id (str):
        body (UpdateDagRunState): Modify the state of a DAG run.

            *New in version 2.2.0*

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAGRun]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            client=client,
            body=body,
        )
    ).parsed
