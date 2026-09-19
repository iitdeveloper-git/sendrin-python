from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kc_idp_hint: None | str | Unset = UNSET,
    return_to: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_kc_idp_hint: None | str | Unset
    if isinstance(kc_idp_hint, Unset):
        json_kc_idp_hint = UNSET
    else:
        json_kc_idp_hint = kc_idp_hint
    params["kc_idp_hint"] = json_kc_idp_hint

    json_return_to: None | str | Unset
    if isinstance(return_to, Unset):
        json_return_to = UNSET
    else:
        json_return_to = return_to
    params["return_to"] = json_return_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/oauth/iitd",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    kc_idp_hint: None | str | Unset = UNSET,
    return_to: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Initiate Central IAM SSO authorization flow

    Args:
        kc_idp_hint (None | str | Unset): Direct IdP hint (e.g. google)
        return_to (None | str | Unset): Frontend return path after login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        kc_idp_hint=kc_idp_hint,
        return_to=return_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    kc_idp_hint: None | str | Unset = UNSET,
    return_to: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Initiate Central IAM SSO authorization flow

    Args:
        kc_idp_hint (None | str | Unset): Direct IdP hint (e.g. google)
        return_to (None | str | Unset): Frontend return path after login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        kc_idp_hint=kc_idp_hint,
        return_to=return_to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    kc_idp_hint: None | str | Unset = UNSET,
    return_to: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Initiate Central IAM SSO authorization flow

    Args:
        kc_idp_hint (None | str | Unset): Direct IdP hint (e.g. google)
        return_to (None | str | Unset): Frontend return path after login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        kc_idp_hint=kc_idp_hint,
        return_to=return_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    kc_idp_hint: None | str | Unset = UNSET,
    return_to: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Initiate Central IAM SSO authorization flow

    Args:
        kc_idp_hint (None | str | Unset): Direct IdP hint (e.g. google)
        return_to (None | str | Unset): Frontend return path after login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            kc_idp_hint=kc_idp_hint,
            return_to=return_to,
        )
    ).parsed
