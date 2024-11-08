from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dag import DAG
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    *,
    fields: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_fields: Union[Unset, List[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DAG]]:
    if response.status_code == 200:
        response_200 = DAG.from_dict(response.json())

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
) -> Response[Union[Any, DAG]]:
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
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, DAG]]:
    """Get basic information about a DAG

     Presents only information available in database (DAGModel).
    If you need detailed information, consider using GET /dags/{dag_id}/details.

    Args:
        dag_id (str):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAG]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, DAG]]:
    """Get basic information about a DAG

     Presents only information available in database (DAGModel).
    If you need detailed information, consider using GET /dags/{dag_id}/details.

    Args:
        dag_id (str):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAG]
    """

    return sync_detailed(
        dag_id=dag_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Response[Union[Any, DAG]]:
    """Get basic information about a DAG

     Presents only information available in database (DAGModel).
    If you need detailed information, consider using GET /dags/{dag_id}/details.

    Args:
        dag_id (str):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DAG]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[Any, DAG]]:
    """Get basic information about a DAG

     Presents only information available in database (DAGModel).
    If you need detailed information, consider using GET /dags/{dag_id}/details.

    Args:
        dag_id (str):
        fields (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DAG]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            client=client,
            fields=fields,
        )
    ).parsed
