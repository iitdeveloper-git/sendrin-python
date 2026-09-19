from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.logout_api_v1_auth_logout_post_response_logout_api_v1_auth_logout_post import (
    LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/logout",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost | None:
    if response.status_code == 200:
        response_200 = LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost]:
    """Log out the current user and invalidate session cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost | None:
    """Log out the current user and invalidate session cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost]:
    """Log out the current user and invalidate session cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost | None:
    """Log out the current user and invalidate session cookie

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LogoutApiV1AuthLogoutPostResponseLogoutApiV1AuthLogoutPost
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
