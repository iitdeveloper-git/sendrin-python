from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_topup_checkout_api_v1_billing_topup_checkout_post_response_billing_topup_checkout_api_v1_billing_topup_checkout_post import (
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.topup_checkout_in import TopupCheckoutIn
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TopupCheckoutIn,
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
        "url": "/api/v1/billing/topup/checkout",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
    | HTTPValidationError
    | None
):
    if response.status_code == 201:
        response_201 = BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost.from_dict(
            response.json()
        )

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
) -> Response[
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
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
    body: TopupCheckoutIn,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
    | HTTPValidationError
]:
    """Start a Razorpay checkout for a credit top-up

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TopupCheckoutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
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
    *,
    client: AuthenticatedClient | Client,
    body: TopupCheckoutIn,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
    | HTTPValidationError
    | None
):
    """Start a Razorpay checkout for a credit top-up

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TopupCheckoutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TopupCheckoutIn,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
    | HTTPValidationError
]:
    """Start a Razorpay checkout for a credit top-up

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TopupCheckoutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TopupCheckoutIn,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost
    | HTTPValidationError
    | None
):
    """Start a Razorpay checkout for a credit top-up

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TopupCheckoutIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingTopupCheckoutApiV1BillingTopupCheckoutPostResponseBillingTopupCheckoutApiV1BillingTopupCheckoutPost | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
