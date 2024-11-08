from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_dag_source_response_200 import GetDagSourceResponse200
from ...types import Response


def _get_kwargs(
    file_token: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/dagSources/{file_token}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetDagSourceResponse200]]:
    if response.status_code == 200:
        response_200 = GetDagSourceResponse200.from_dict(response.json())

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
    if response.status_code == 406:
        response_406 = cast(Any, None)
        return response_406
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetDagSourceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetDagSourceResponse200]]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDagSourceResponse200]]
    """

    kwargs = _get_kwargs(
        file_token=file_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDagSourceResponse200]]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDagSourceResponse200]
    """

    return sync_detailed(
        file_token=file_token,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetDagSourceResponse200]]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDagSourceResponse200]]
    """

    kwargs = _get_kwargs(
        file_token=file_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_token: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDagSourceResponse200]]:
    """Get a source code

     Get a source code using file token.

    Args:
        file_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDagSourceResponse200]
    """

    return (
        await asyncio_detailed(
            file_token=file_token,
            client=client,
        )
    ).parsed
