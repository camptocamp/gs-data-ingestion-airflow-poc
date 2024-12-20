from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    dag_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/dags/{dag_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 409:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Delete a DAG

     Deletes all metadata related to the DAG, including finished DAG Runs and Tasks.
    Logs are not deleted. This action cannot be undone.

    *New in version 2.2.0*

    Args:
        dag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
