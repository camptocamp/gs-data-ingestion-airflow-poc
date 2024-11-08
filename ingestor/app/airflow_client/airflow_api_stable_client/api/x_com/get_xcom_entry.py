from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.x_com import XCom
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    map_index: Union[Unset, int] = UNSET,
    deserialize: Union[Unset, bool] = False,
    stringify: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["map_index"] = map_index

    params["deserialize"] = deserialize

    params["stringify"] = stringify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, XCom]]:
    if response.status_code == 200:
        response_200 = XCom.from_dict(response.json())

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
) -> Response[Union[Any, XCom]]:
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
    xcom_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    map_index: Union[Unset, int] = UNSET,
    deserialize: Union[Unset, bool] = False,
    stringify: Union[Unset, bool] = True,
) -> Response[Union[Any, XCom]]:
    """Get an XCom entry

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (Union[Unset, int]):
        deserialize (Union[Unset, bool]):  Default: False.
        stringify (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, XCom]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    map_index: Union[Unset, int] = UNSET,
    deserialize: Union[Unset, bool] = False,
    stringify: Union[Unset, bool] = True,
) -> Optional[Union[Any, XCom]]:
    """Get an XCom entry

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (Union[Unset, int]):
        deserialize (Union[Unset, bool]):  Default: False.
        stringify (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, XCom]
    """

    return sync_detailed(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        client=client,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    ).parsed


async def asyncio_detailed(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    map_index: Union[Unset, int] = UNSET,
    deserialize: Union[Unset, bool] = False,
    stringify: Union[Unset, bool] = True,
) -> Response[Union[Any, XCom]]:
    """Get an XCom entry

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (Union[Unset, int]):
        deserialize (Union[Unset, bool]):  Default: False.
        stringify (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, XCom]]
    """

    kwargs = _get_kwargs(
        dag_id=dag_id,
        dag_run_id=dag_run_id,
        task_id=task_id,
        xcom_key=xcom_key,
        map_index=map_index,
        deserialize=deserialize,
        stringify=stringify,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dag_id: str,
    dag_run_id: str,
    task_id: str,
    xcom_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
    map_index: Union[Unset, int] = UNSET,
    deserialize: Union[Unset, bool] = False,
    stringify: Union[Unset, bool] = True,
) -> Optional[Union[Any, XCom]]:
    """Get an XCom entry

    Args:
        dag_id (str):
        dag_run_id (str):
        task_id (str):
        xcom_key (str):
        map_index (Union[Unset, int]):
        deserialize (Union[Unset, bool]):  Default: False.
        stringify (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, XCom]
    """

    return (
        await asyncio_detailed(
            dag_id=dag_id,
            dag_run_id=dag_run_id,
            task_id=task_id,
            xcom_key=xcom_key,
            client=client,
            map_index=map_index,
            deserialize=deserialize,
            stringify=stringify,
        )
    ).parsed
