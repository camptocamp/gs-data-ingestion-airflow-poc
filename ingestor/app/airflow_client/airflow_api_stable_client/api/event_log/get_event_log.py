from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_log import EventLog
from ...types import Response


def _get_kwargs(
    event_log_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/eventLogs/{event_log_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventLog]]:
    if response.status_code == 200:
        response_200 = EventLog.from_dict(response.json())

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
) -> Response[Union[Any, EventLog]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_log_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, EventLog]]:
    """Get a log entry

    Args:
        event_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventLog]]
    """

    kwargs = _get_kwargs(
        event_log_id=event_log_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_log_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, EventLog]]:
    """Get a log entry

    Args:
        event_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventLog]
    """

    return sync_detailed(
        event_log_id=event_log_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_log_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, EventLog]]:
    """Get a log entry

    Args:
        event_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventLog]]
    """

    kwargs = _get_kwargs(
        event_log_id=event_log_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_log_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, EventLog]]:
    """Get a log entry

    Args:
        event_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventLog]
    """

    return (
        await asyncio_detailed(
            event_log_id=event_log_id,
            client=client,
        )
    ).parsed
