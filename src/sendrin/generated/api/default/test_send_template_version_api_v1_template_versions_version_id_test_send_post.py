from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.template_test_send import TemplateTestSend
from ...models.test_send_template_version_api_v1_template_versions_version_id_test_send_post_response_test_send_template_version_api_v1_template_versions_version_id_test_send_post import (
    TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str,
    *,
    body: TemplateTestSend,
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
        "url": "/api/v1/template-versions/{version_id}/test-send".format(
            version_id=quote(str(version_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
    | None
):
    if response.status_code == 200:
        response_200 = TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost.from_dict(
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
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemplateTestSend,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
]:
    """Test Send Template Version

    Args:
        version_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TemplateTestSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
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
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemplateTestSend,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
    | None
):
    """Test Send Template Version

    Args:
        version_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TemplateTestSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemplateTestSend,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
]:
    """Test Send Template Version

    Args:
        version_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TemplateTestSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        body=body,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TemplateTestSend,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
    | None
):
    """Test Send Template Version

    Args:
        version_id (str):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):
        body (TemplateTestSend):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPostResponseTestSendTemplateVersionApiV1TemplateVersionsVersionIdTestSendPost
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            body=body,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
