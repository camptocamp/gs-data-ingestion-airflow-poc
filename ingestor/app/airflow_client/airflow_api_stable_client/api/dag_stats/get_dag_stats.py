from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag_stats_collection_schema import DagStatsCollectionSchema
from ...types import UNSET, Response


def _get_kwargs(
    *,
    dag_ids: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["dag_ids"] = dag_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/dagStats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DagStatsCollectionSchema]]:
    if response.status_code == 200:
        response_200 = DagStatsCollectionSchema.from_dict(response.json())

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
) -> Response[Union[Any, DagStatsCollectionSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_ids: str,
) -> Response[Union[Any, DagStatsCollectionSchema]]:
    """List Dag statistics

    Args:
        dag_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DagStatsCollectionSchema]]
    """

    kwargs = _get_kwargs(
        dag_ids=dag_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_ids: str,
) -> Optional[Union[Any, DagStatsCollectionSchema]]:
    """List Dag statistics

    Args:
        dag_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DagStatsCollectionSchema]
    """

    return sync_detailed(
        client=client,
        dag_ids=dag_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_ids: str,
) -> Response[Union[Any, DagStatsCollectionSchema]]:
    """List Dag statistics

    Args:
        dag_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DagStatsCollectionSchema]]
    """

    kwargs = _get_kwargs(
        dag_ids=dag_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    dag_ids: str,
) -> Optional[Union[Any, DagStatsCollectionSchema]]:
    """List Dag statistics

    Args:
        dag_ids (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DagStatsCollectionSchema]
    """

    return (
        await asyncio_detailed(
            client=client,
            dag_ids=dag_ids,
        )
    ).parsed