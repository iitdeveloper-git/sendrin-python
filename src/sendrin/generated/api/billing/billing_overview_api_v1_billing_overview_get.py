from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_overview_api_v1_billing_overview_get_response_billing_overview_api_v1_billing_overview_get import (
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "/api/v1/billing/overview",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet.from_dict(
            response.json()
        )

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
) -> Response[
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
]:
    """Current plan, entitlements, and credit balances

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
    | None
):
    """Current plan, entitlements, and credit balances

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
]:
    """Current plan, entitlements, and credit balances

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet
    | HTTPValidationError
    | None
):
    """Current plan, entitlements, and credit balances

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingOverviewApiV1BillingOverviewGetResponseBillingOverviewApiV1BillingOverviewGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
