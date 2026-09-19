from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.in_app_unread_count import InAppUnreadCount
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
    x_app_id: None | str | Unset = UNSET,
    x_session_id: None | str | Unset = UNSET,
    x_gns_user_roles: None | str | Unset = UNSET,
    x_gns_user_groups: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    if not isinstance(x_tenant_id, Unset):
        headers["x-tenant-id"] = x_tenant_id

    if not isinstance(x_app_id, Unset):
        headers["x-app-id"] = x_app_id

    if not isinstance(x_session_id, Unset):
        headers["x-session-id"] = x_session_id

    if not isinstance(x_gns_user_roles, Unset):
        headers["x-gns-user-roles"] = x_gns_user_roles

    if not isinstance(x_gns_user_groups, Unset):
        headers["x-gns-user-groups"] = x_gns_user_groups

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/in-app/unread-count",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InAppUnreadCount | None:
    if response.status_code == 200:
        response_200 = InAppUnreadCount.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | InAppUnreadCount]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
    x_app_id: None | str | Unset = UNSET,
    x_session_id: None | str | Unset = UNSET,
    x_gns_user_roles: None | str | Unset = UNSET,
    x_gns_user_groups: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InAppUnreadCount]:
    """Unread Count

    Args:
        authorization (None | str | Unset):
        x_tenant_id (None | str | Unset):
        x_app_id (None | str | Unset):
        x_session_id (None | str | Unset):
        x_gns_user_roles (None | str | Unset):
        x_gns_user_groups (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InAppUnreadCount]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_tenant_id=x_tenant_id,
        x_app_id=x_app_id,
        x_session_id=x_session_id,
        x_gns_user_roles=x_gns_user_roles,
        x_gns_user_groups=x_gns_user_groups,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
    x_app_id: None | str | Unset = UNSET,
    x_session_id: None | str | Unset = UNSET,
    x_gns_user_roles: None | str | Unset = UNSET,
    x_gns_user_groups: None | str | Unset = UNSET,
) -> HTTPValidationError | InAppUnreadCount | None:
    """Unread Count

    Args:
        authorization (None | str | Unset):
        x_tenant_id (None | str | Unset):
        x_app_id (None | str | Unset):
        x_session_id (None | str | Unset):
        x_gns_user_roles (None | str | Unset):
        x_gns_user_groups (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InAppUnreadCount
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
        x_tenant_id=x_tenant_id,
        x_app_id=x_app_id,
        x_session_id=x_session_id,
        x_gns_user_roles=x_gns_user_roles,
        x_gns_user_groups=x_gns_user_groups,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
    x_app_id: None | str | Unset = UNSET,
    x_session_id: None | str | Unset = UNSET,
    x_gns_user_roles: None | str | Unset = UNSET,
    x_gns_user_groups: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InAppUnreadCount]:
    """Unread Count

    Args:
        authorization (None | str | Unset):
        x_tenant_id (None | str | Unset):
        x_app_id (None | str | Unset):
        x_session_id (None | str | Unset):
        x_gns_user_roles (None | str | Unset):
        x_gns_user_groups (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InAppUnreadCount]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_tenant_id=x_tenant_id,
        x_app_id=x_app_id,
        x_session_id=x_session_id,
        x_gns_user_roles=x_gns_user_roles,
        x_gns_user_groups=x_gns_user_groups,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
    x_app_id: None | str | Unset = UNSET,
    x_session_id: None | str | Unset = UNSET,
    x_gns_user_roles: None | str | Unset = UNSET,
    x_gns_user_groups: None | str | Unset = UNSET,
) -> HTTPValidationError | InAppUnreadCount | None:
    """Unread Count

    Args:
        authorization (None | str | Unset):
        x_tenant_id (None | str | Unset):
        x_app_id (None | str | Unset):
        x_session_id (None | str | Unset):
        x_gns_user_roles (None | str | Unset):
        x_gns_user_groups (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InAppUnreadCount
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
            x_tenant_id=x_tenant_id,
            x_app_id=x_app_id,
            x_session_id=x_session_id,
            x_gns_user_roles=x_gns_user_roles,
            x_gns_user_groups=x_gns_user_groups,
        )
    ).parsed
