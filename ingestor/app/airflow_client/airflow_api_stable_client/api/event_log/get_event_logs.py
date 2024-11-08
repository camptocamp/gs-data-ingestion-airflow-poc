import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_log_collection import EventLogCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dag_id: Union[Unset, str] = UNSET,
    task_id: Union[Unset, str] = UNSET,
    run_id: Union[Unset, str] = UNSET,
    map_index: Union[Unset, int] = UNSET,
    try_number: Union[Unset, int] = UNSET,
    event: Union[Unset, str] = UNSET,
    owner: Union[Unset, str] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    included_events: Union[Unset, str] = UNSET,
    excluded_events: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["order_by"] = order_by

    params["dag_id"] = dag_id

    params["task_id"] = task_id

    params["run_id"] = run_id

    params["map_index"] = map_index

    params["try_number"] = try_number

    params["event"] = event

    params["owner"] = owner

    json_before: Union[Unset, str] = UNSET
    if not isinstance(before, Unset):
        json_before = before.isoformat()
    params["before"] = json_before

    json_after: Union[Unset, str] = UNSET
    if not isinstance(after, Unset):
        json_after = after.isoformat()
    params["after"] = json_after

    params["included_events"] = included_events

    params["excluded_events"] = excluded_events

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/eventLogs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventLogCollection]]:
    if response.status_code == 200:
        response_200 = EventLogCollection.from_dict(response.json())

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
) -> Response[Union[Any, EventLogCollection]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dag_id: Union[Unset, str] = UNSET,
    task_id: Union[Unset, str] = UNSET,
    run_id: Union[Unset, str] = UNSET,
    map_index: Union[Unset, int] = UNSET,
    try_number: Union[Unset, int] = UNSET,
    event: Union[Unset, str] = UNSET,
    owner: Union[Unset, str] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    included_events: Union[Unset, str] = UNSET,
    excluded_events: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventLogCollection]]:
    """List log entries

     List log entries from event log.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dag_id (Union[Unset, str]):
        task_id (Union[Unset, str]):
        run_id (Union[Unset, str]):
        map_index (Union[Unset, int]):
        try_number (Union[Unset, int]):
        event (Union[Unset, str]):
        owner (Union[Unset, str]):
        before (Union[Unset, datetime.datetime]):
        after (Union[Unset, datetime.datetime]):
        included_events (Union[Unset, str]):
        excluded_events (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventLogCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dag_id: Union[Unset, str] = UNSET,
    task_id: Union[Unset, str] = UNSET,
    run_id: Union[Unset, str] = UNSET,
    map_index: Union[Unset, int] = UNSET,
    try_number: Union[Unset, int] = UNSET,
    event: Union[Unset, str] = UNSET,
    owner: Union[Unset, str] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    included_events: Union[Unset, str] = UNSET,
    excluded_events: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventLogCollection]]:
    """List log entries

     List log entries from event log.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dag_id (Union[Unset, str]):
        task_id (Union[Unset, str]):
        run_id (Union[Unset, str]):
        map_index (Union[Unset, int]):
        try_number (Union[Unset, int]):
        event (Union[Unset, str]):
        owner (Union[Unset, str]):
        before (Union[Unset, datetime.datetime]):
        after (Union[Unset, datetime.datetime]):
        included_events (Union[Unset, str]):
        excluded_events (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventLogCollection]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dag_id: Union[Unset, str] = UNSET,
    task_id: Union[Unset, str] = UNSET,
    run_id: Union[Unset, str] = UNSET,
    map_index: Union[Unset, int] = UNSET,
    try_number: Union[Unset, int] = UNSET,
    event: Union[Unset, str] = UNSET,
    owner: Union[Unset, str] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    included_events: Union[Unset, str] = UNSET,
    excluded_events: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EventLogCollection]]:
    """List log entries

     List log entries from event log.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dag_id (Union[Unset, str]):
        task_id (Union[Unset, str]):
        run_id (Union[Unset, str]):
        map_index (Union[Unset, int]):
        try_number (Union[Unset, int]):
        event (Union[Unset, str]):
        owner (Union[Unset, str]):
        before (Union[Unset, datetime.datetime]):
        after (Union[Unset, datetime.datetime]):
        included_events (Union[Unset, str]):
        excluded_events (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventLogCollection]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_by=order_by,
        dag_id=dag_id,
        task_id=task_id,
        run_id=run_id,
        map_index=map_index,
        try_number=try_number,
        event=event,
        owner=owner,
        before=before,
        after=after,
        included_events=included_events,
        excluded_events=excluded_events,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = UNSET,
    order_by: Union[Unset, str] = UNSET,
    dag_id: Union[Unset, str] = UNSET,
    task_id: Union[Unset, str] = UNSET,
    run_id: Union[Unset, str] = UNSET,
    map_index: Union[Unset, int] = UNSET,
    try_number: Union[Unset, int] = UNSET,
    event: Union[Unset, str] = UNSET,
    owner: Union[Unset, str] = UNSET,
    before: Union[Unset, datetime.datetime] = UNSET,
    after: Union[Unset, datetime.datetime] = UNSET,
    included_events: Union[Unset, str] = UNSET,
    excluded_events: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EventLogCollection]]:
    """List log entries

     List log entries from event log.

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):
        order_by (Union[Unset, str]):
        dag_id (Union[Unset, str]):
        task_id (Union[Unset, str]):
        run_id (Union[Unset, str]):
        map_index (Union[Unset, int]):
        try_number (Union[Unset, int]):
        event (Union[Unset, str]):
        owner (Union[Unset, str]):
        before (Union[Unset, datetime.datetime]):
        after (Union[Unset, datetime.datetime]):
        included_events (Union[Unset, str]):
        excluded_events (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventLogCollection]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_by=order_by,
            dag_id=dag_id,
            task_id=task_id,
            run_id=run_id,
            map_index=map_index,
            try_number=try_number,
            event=event,
            owner=owner,
            before=before,
            after=after,
            included_events=included_events,
            excluded_events=excluded_events,
        )
    ).parsed
