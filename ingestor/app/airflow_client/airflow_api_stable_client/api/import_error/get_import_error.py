from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_error import ImportError_
from ...types import Response


def _get_kwargs(
    import_error_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/importErrors/{import_error_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ImportError_]]:
    if response.status_code == 200:
        response_200 = ImportError_.from_dict(response.json())

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
) -> Response[Union[Any, ImportError_]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    import_error_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ImportError_]]:
    """Get an import error

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImportError_]]
    """

    kwargs = _get_kwargs(
        import_error_id=import_error_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    import_error_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ImportError_]]:
    """Get an import error

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImportError_]
    """

    return sync_detailed(
        import_error_id=import_error_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    import_error_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ImportError_]]:
    """Get an import error

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ImportError_]]
    """

    kwargs = _get_kwargs(
        import_error_id=import_error_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    import_error_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ImportError_]]:
    """Get an import error

    Args:
        import_error_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ImportError_]
    """

    return (
        await asyncio_detailed(
            import_error_id=import_error_id,
            client=client,
        )
    ).parsed
