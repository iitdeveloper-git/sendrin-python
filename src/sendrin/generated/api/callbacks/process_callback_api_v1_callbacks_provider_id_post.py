from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.process_callback_api_v1_callbacks_provider_id_post_response_process_callback_api_v1_callbacks_provider_id_post import (
    ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost,
)
from ...types import Response


def _get_kwargs(
    provider_id: str,
    *,
    x_gns_callback_timestamp: str,
    x_gns_callback_signature: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-GNS-Callback-Timestamp"] = x_gns_callback_timestamp

    headers["X-GNS-Callback-Signature"] = x_gns_callback_signature

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/callbacks/{provider_id}".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
    | None
):
    if response.status_code == 202:
        response_202 = ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost.from_dict(
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
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_gns_callback_timestamp: str,
    x_gns_callback_signature: str,
) -> Response[
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
]:
    """Process Callback

    Args:
        provider_id (str):
        x_gns_callback_timestamp (str):
        x_gns_callback_signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        x_gns_callback_timestamp=x_gns_callback_timestamp,
        x_gns_callback_signature=x_gns_callback_signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_gns_callback_timestamp: str,
    x_gns_callback_signature: str,
) -> (
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
    | None
):
    """Process Callback

    Args:
        provider_id (str):
        x_gns_callback_timestamp (str):
        x_gns_callback_signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        x_gns_callback_timestamp=x_gns_callback_timestamp,
        x_gns_callback_signature=x_gns_callback_signature,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_gns_callback_timestamp: str,
    x_gns_callback_signature: str,
) -> Response[
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
]:
    """Process Callback

    Args:
        provider_id (str):
        x_gns_callback_timestamp (str):
        x_gns_callback_signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost]
    """

    kwargs = _get_kwargs(
        provider_id=provider_id,
        x_gns_callback_timestamp=x_gns_callback_timestamp,
        x_gns_callback_signature=x_gns_callback_signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_gns_callback_timestamp: str,
    x_gns_callback_signature: str,
) -> (
    HTTPValidationError
    | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
    | None
):
    """Process Callback

    Args:
        provider_id (str):
        x_gns_callback_timestamp (str):
        x_gns_callback_signature (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProcessCallbackApiV1CallbacksProviderIdPostResponseProcessCallbackApiV1CallbacksProviderIdPost
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            x_gns_callback_timestamp=x_gns_callback_timestamp,
            x_gns_callback_signature=x_gns_callback_signature,
        )
    ).parsed
