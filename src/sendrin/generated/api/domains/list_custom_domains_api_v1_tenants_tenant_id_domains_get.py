from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_list_response import DomainListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_id: str,
    *,
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
        "method": "get",
        "url": "/api/v1/tenants/{tenant_id}/domains".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DomainListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DomainListResponse.from_dict(response.json())

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
) -> Response[DomainListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[DomainListResponse | HTTPValidationError]:
    """List Custom Domains

    Args:
        tenant_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> DomainListResponse | HTTPValidationError | None:
    """List Custom Domains

    Args:
        tenant_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainListResponse | HTTPValidationError
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    tenant_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[DomainListResponse | HTTPValidationError]:
    """List Custom Domains

    Args:
        tenant_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> DomainListResponse | HTTPValidationError | None:
    """List Custom Domains

    Args:
        tenant_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
