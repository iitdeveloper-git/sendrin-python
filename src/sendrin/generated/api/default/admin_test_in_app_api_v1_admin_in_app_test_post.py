from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_test_in_app_api_v1_admin_in_app_test_post_response_admin_test_in_app_api_v1_admin_in_app_test_post import (
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.in_app_admin_test import InAppAdminTest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: InAppAdminTest,
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
        "url": "/api/v1/admin/in-app/test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
    | HTTPValidationError
    | None
):
    if response.status_code == 202:
        response_202 = AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost.from_dict(
            response.json()
        )

        return response_202

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
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
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
    client: AuthenticatedClient,
    body: InAppAdminTest,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
    | HTTPValidationError
]:
    """Admin Test In App

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (InAppAdminTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost | HTTPValidationError]
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
    client: AuthenticatedClient,
    body: InAppAdminTest,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
    | HTTPValidationError
    | None
):
    """Admin Test In App

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (InAppAdminTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost | HTTPValidationError
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
    client: AuthenticatedClient,
    body: InAppAdminTest,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
    | HTTPValidationError
]:
    """Admin Test In App

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (InAppAdminTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost | HTTPValidationError]
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
    client: AuthenticatedClient,
    body: InAppAdminTest,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost
    | HTTPValidationError
    | None
):
    """Admin Test In App

    Args:
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (InAppAdminTest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminTestInAppApiV1AdminInAppTestPostResponseAdminTestInAppApiV1AdminInAppTestPost | HTTPValidationError
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
