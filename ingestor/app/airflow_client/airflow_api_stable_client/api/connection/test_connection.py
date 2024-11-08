from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection import Connection
from ...models.connection_test import ConnectionTest
from ...types import Response


def _get_kwargs(
    *,
    body: Connection,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/connections/test",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ConnectionTest]]:
    if response.status_code == 200:
        response_200 = ConnectionTest.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, ConnectionTest]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Connection,
) -> Response[Union[Any, ConnectionTest]]:
    r"""Test a connection

     Test a connection.

    For security reasons, the test connection functionality is disabled by default across Airflow UI,
    API and CLI.
    For more information on capabilities of users, see the documentation:
    https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html#capabilities-of-
    authenticated-ui-users.
    It is strongly advised to not enable the feature until you make sure that only
    highly trusted UI/API users have \"edit connection\" permissions.

    Set the \"test_connection\" flag to \"Enabled\" in the \"core\" section of Airflow configuration
    (airflow.cfg) to enable testing of collections.
    It can also be controlled by the environment variable `AIRFLOW__CORE__TEST_CONNECTION`.

    *New in version 2.2.0*

    Args:
        body (Connection): Full representation of the connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConnectionTest]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Connection,
) -> Optional[Union[Any, ConnectionTest]]:
    r"""Test a connection

     Test a connection.

    For security reasons, the test connection functionality is disabled by default across Airflow UI,
    API and CLI.
    For more information on capabilities of users, see the documentation:
    https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html#capabilities-of-
    authenticated-ui-users.
    It is strongly advised to not enable the feature until you make sure that only
    highly trusted UI/API users have \"edit connection\" permissions.

    Set the \"test_connection\" flag to \"Enabled\" in the \"core\" section of Airflow configuration
    (airflow.cfg) to enable testing of collections.
    It can also be controlled by the environment variable `AIRFLOW__CORE__TEST_CONNECTION`.

    *New in version 2.2.0*

    Args:
        body (Connection): Full representation of the connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConnectionTest]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Connection,
) -> Response[Union[Any, ConnectionTest]]:
    r"""Test a connection

     Test a connection.

    For security reasons, the test connection functionality is disabled by default across Airflow UI,
    API and CLI.
    For more information on capabilities of users, see the documentation:
    https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html#capabilities-of-
    authenticated-ui-users.
    It is strongly advised to not enable the feature until you make sure that only
    highly trusted UI/API users have \"edit connection\" permissions.

    Set the \"test_connection\" flag to \"Enabled\" in the \"core\" section of Airflow configuration
    (airflow.cfg) to enable testing of collections.
    It can also be controlled by the environment variable `AIRFLOW__CORE__TEST_CONNECTION`.

    *New in version 2.2.0*

    Args:
        body (Connection): Full representation of the connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ConnectionTest]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Connection,
) -> Optional[Union[Any, ConnectionTest]]:
    r"""Test a connection

     Test a connection.

    For security reasons, the test connection functionality is disabled by default across Airflow UI,
    API and CLI.
    For more information on capabilities of users, see the documentation:
    https://airflow.apache.org/docs/apache-airflow/stable/security/security_model.html#capabilities-of-
    authenticated-ui-users.
    It is strongly advised to not enable the feature until you make sure that only
    highly trusted UI/API users have \"edit connection\" permissions.

    Set the \"test_connection\" flag to \"Enabled\" in the \"core\" section of Airflow configuration
    (airflow.cfg) to enable testing of collections.
    It can also be controlled by the environment variable `AIRFLOW__CORE__TEST_CONNECTION`.

    *New in version 2.2.0*

    Args:
        body (Connection): Full representation of the connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ConnectionTest]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
