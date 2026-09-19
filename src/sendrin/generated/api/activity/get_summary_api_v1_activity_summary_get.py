import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_summary_response import ActivitySummaryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    application_id: None | str | Unset = UNSET,
    product: None | str | Unset = UNSET,
    channel: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
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

    params: dict[str, Any] = {}

    json_application_id: None | str | Unset
    if isinstance(application_id, Unset):
        json_application_id = UNSET
    else:
        json_application_id = application_id
    params["application_id"] = json_application_id

    json_product: None | str | Unset
    if isinstance(product, Unset):
        json_product = UNSET
    else:
        json_product = product
    params["product"] = json_product

    json_channel: None | str | Unset
    if isinstance(channel, Unset):
        json_channel = UNSET
    else:
        json_channel = channel
    params["channel"] = json_channel

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_date_from: None | str | Unset
    if isinstance(date_from, Unset):
        json_date_from = UNSET
    elif isinstance(date_from, datetime.datetime):
        json_date_from = date_from.isoformat()
    else:
        json_date_from = date_from
    params["date_from"] = json_date_from

    json_date_to: None | str | Unset
    if isinstance(date_to, Unset):
        json_date_to = UNSET
    elif isinstance(date_to, datetime.datetime):
        json_date_to = date_to.isoformat()
    else:
        json_date_to = date_to
    params["date_to"] = json_date_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/activity/summary",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivitySummaryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ActivitySummaryResponse.from_dict(response.json())

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
) -> Response[ActivitySummaryResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    application_id: None | str | Unset = UNSET,
    product: None | str | Unset = UNSET,
    channel: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[ActivitySummaryResponse | HTTPValidationError]:
    """Get Summary

    Args:
        application_id (None | str | Unset):
        product (None | str | Unset):
        channel (None | str | Unset):
        search (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitySummaryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        product=product,
        channel=channel,
        search=search,
        date_from=date_from,
        date_to=date_to,
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
    application_id: None | str | Unset = UNSET,
    product: None | str | Unset = UNSET,
    channel: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> ActivitySummaryResponse | HTTPValidationError | None:
    """Get Summary

    Args:
        application_id (None | str | Unset):
        product (None | str | Unset):
        channel (None | str | Unset):
        search (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitySummaryResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        application_id=application_id,
        product=product,
        channel=channel,
        search=search,
        date_from=date_from,
        date_to=date_to,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    application_id: None | str | Unset = UNSET,
    product: None | str | Unset = UNSET,
    channel: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> Response[ActivitySummaryResponse | HTTPValidationError]:
    """Get Summary

    Args:
        application_id (None | str | Unset):
        product (None | str | Unset):
        channel (None | str | Unset):
        search (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitySummaryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
        product=product,
        channel=channel,
        search=search,
        date_from=date_from,
        date_to=date_to,
        x_admin_user=x_admin_user,
        x_admin_roles=x_admin_roles,
        x_tenant_id=x_tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    application_id: None | str | Unset = UNSET,
    product: None | str | Unset = UNSET,
    channel: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    x_admin_user: None | str | Unset = UNSET,
    x_admin_roles: None | str | Unset = UNSET,
    x_tenant_id: None | str | Unset = UNSET,
) -> ActivitySummaryResponse | HTTPValidationError | None:
    """Get Summary

    Args:
        application_id (None | str | Unset):
        product (None | str | Unset):
        channel (None | str | Unset):
        search (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        x_admin_user (None | str | Unset):
        x_admin_roles (None | str | Unset):
        x_tenant_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitySummaryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            application_id=application_id,
            product=product,
            channel=channel,
            search=search,
            date_from=date_from,
            date_to=date_to,
            x_admin_user=x_admin_user,
            x_admin_roles=x_admin_roles,
            x_tenant_id=x_tenant_id,
        )
    ).parsed
