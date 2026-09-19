from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_create import CredentialCreate
from ...models.credential_secret import CredentialSecret
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    app_id: str,
    *,
    body: CredentialCreate,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_admin_user, Unset):
        headers["x-admin-user"] = x_admin_user

    if not isinstance(x_admin_roles, Unset):
        headers["x-admin-roles"] = x_admin_roles

    if not isinstance(x_tenant_id, Unset):
        headers["x-tenant-id"] = x_tenant_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/apps/{app_id}/credentials".format(
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CredentialSecret | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = CredentialSecret.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CredentialSecret | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialCreate,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[CredentialSecret | HTTPValidationError]:
    """Create Credential

    Args:
        app_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (CredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialSecret | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialCreate,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> CredentialSecret | HTTPValidationError | None:
    """Create Credential

    Args:
        app_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (CredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialSecret | HTTPValidationError
    """

    return sync_detailed(
        app_id=app_id,
        client=client,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialCreate,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[CredentialSecret | HTTPValidationError]:
    """Create Credential

    Args:
        app_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (CredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialSecret | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialCreate,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> CredentialSecret | HTTPValidationError | None:
    """Create Credential

    Args:
        app_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (CredentialCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialSecret | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            app_id=app_id,
            client=client,
            body=body,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
