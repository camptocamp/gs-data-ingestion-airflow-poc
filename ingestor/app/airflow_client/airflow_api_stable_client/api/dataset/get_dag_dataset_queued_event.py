import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.queued_event import QueuedEvent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    uri: str,
    *,
    before: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_before: Union[Unset, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}/datasets/queuedEvent/{uri}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, QueuedEvent]]:
    if response.status_code == 200:
        response_200 = QueuedEvent.from_dict(response.json())

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
) -> Response[Union[Any, QueuedEvent]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dag_id: str,
    uri: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, QueuedEvent]]:
    """Get a queued Dataset event for a DAG

     Get a queued Dataset event for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        uri (str):
        before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueuedEvent]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        uri=uri,
        before=before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    uri: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, QueuedEvent]]:
    """Get a queued Dataset event for a DAG

     Get a queued Dataset event for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        uri (str):
        before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueuedEvent]
    """

    return sync_detailed(
        dag_id=dag_id,
        uri=uri,
        client=client,
        before=before,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    uri: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, QueuedEvent]]:
    """Get a queued Dataset event for a DAG

     Get a queued Dataset event for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        uri (str):
        before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueuedEvent]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        uri=uri,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    uri: str,
    *,
    client: Union[AuthenticatedClient, Client],
    before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, QueuedEvent]]:
    """Get a queued Dataset event for a DAG

     Get a queued Dataset event for a DAG.

    *New in version 2.9.0*

    Args:
        dag_id (str):
        uri (str):
        before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueuedEvent]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            uri=uri,
            client=client,
            before=before,
        )
    ).parsed
