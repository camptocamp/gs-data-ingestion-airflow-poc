from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.variable import Variable
from ...types import Response


def _get_kwargs(
    variable_key: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/variables/{variable_key}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Variable]]:
    if response.status_code == 200:
        response_200 = Variable.from_dict(response.json())

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
) -> Response[Union[Any, Variable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    variable_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Variable]]:
    """Get a variable

     Get a variable by key.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Variable]]
    """

    kwargs = _get_kwargs(
        variable_key=variable_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    variable_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Variable]]:
    """Get a variable

     Get a variable by key.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Variable]
    """

    return sync_detailed(
        variable_key=variable_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    variable_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Variable]]:
    """Get a variable

     Get a variable by key.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Variable]]
    """

    kwargs = _get_kwargs(
        variable_key=variable_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    variable_key: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Variable]]:
    """Get a variable

     Get a variable by key.

    Args:
        variable_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Variable]
    """

    return (
        await asyncio_detailed(
            variable_key=variable_key,
            client=client,
        )
    ).parsed
