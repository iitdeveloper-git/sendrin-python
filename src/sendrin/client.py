from __future__ import annotations

import time
from typing import Any, cast

import httpx

from sendrin.exceptions import SendrinAPIError, SendrinQuotaExceededError
from sendrin.generated.models.send_otp_request import SendOtpRequest
from sendrin.generated.models.send_otp_request_channel import SendOtpRequestChannel
from sendrin.generated.models.send_otp_response import SendOtpResponse
from sendrin.generated.models.verify_otp_request import VerifyOtpRequest
from sendrin.generated.models.verify_otp_request_channel import VerifyOtpRequestChannel
from sendrin.generated.models.verify_otp_response import VerifyOtpResponse
from sendrin.generated.types import UNSET


class Sendrin:
    """Thin, typed wrapper around the generated Sendrin API client.

    >>> client = Sendrin(api_key="gns_live_sk_...")
    >>> client.otp.send(channel="sms", recipient_phone="+14155552671", purpose="login")
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.sendrin.com",
        timeout_seconds: float = 10.0,
        max_retries: int = 2,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds
        self._max_retries = max_retries
        self._http = httpx.Client(
            base_url=self._base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout_seconds,
            transport=transport,
        )
        self.otp = _OtpNamespace(self)

    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        last_exc: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                response = self._http.request(method, path, **kwargs)
            except httpx.TransportError as exc:
                last_exc = exc
                if attempt < self._max_retries:
                    time.sleep(0.5 * (2**attempt))
                    continue
                raise SendrinAPIError(f"Network error calling Sendrin API: {exc}") from exc

            if response.status_code == 429:
                detail = _safe_json(response)
                # Quota exceeded is not retryable — retrying immediately just
                # fails again and burns another request against the same quota.
                raise SendrinQuotaExceededError(
                    detail.get("detail", {}).get("message", "Quota exceeded"),
                    status_code=429,
                )
            if response.status_code >= 500 and attempt < self._max_retries:
                time.sleep(0.5 * (2**attempt))
                continue
            if response.status_code >= 400:
                detail = _safe_json(response)
                raise SendrinAPIError(
                    detail.get("detail", {}).get("message", response.text),
                    status_code=response.status_code,
                    error_code=detail.get("detail", {}).get("code"),
                )
            return _safe_json(response)
        raise SendrinAPIError(f"Request failed after {self._max_retries} retries") from last_exc

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> Sendrin:
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.close()


def _safe_json(response: httpx.Response) -> dict[str, Any]:
    try:
        return cast(dict[str, Any], response.json())
    except ValueError:
        return {}


class _OtpNamespace:
    """Convenience wrapper around the generated OTP endpoints.

    Builds requests/parses responses using the generated request and response
    models (`sendrin.generated.models`), but sends them through the parent
    `Sendrin` instance's `_request` method so that OTP calls get the same
    retry, quota, and error-handling behavior as every other call made
    through this SDK.
    """

    def __init__(self, client: Sendrin) -> None:
        self._client = client

    def send(
        self,
        channel: str,
        recipient_phone: str | None = None,
        recipient_email: str | None = None,
        purpose: str = "login",
        code: str | None = None,
        **kwargs: Any,
    ) -> SendOtpResponse:
        # `code_length`/`ttl_seconds` carry server-side defaults. The generated
        # SendOtpRequest dataclass bakes the OpenAPI spec's documented default
        # values (6, 600) directly into its own field defaults rather than
        # UNSET, so leaving them out of this call would silently still send
        # those literal values. Default them to UNSET here instead so, unless
        # a caller explicitly passes one, the field is omitted from the
        # request body entirely and the server applies its own current
        # default — this is what keeps the SDK from drifting out of sync if
        # that server-side default ever changes without a client regen.
        kwargs.setdefault("code_length", UNSET)
        kwargs.setdefault("ttl_seconds", UNSET)
        request = SendOtpRequest(
            channel=SendOtpRequestChannel(channel),
            recipient_email=recipient_email,
            recipient_phone=recipient_phone,
            purpose=purpose,
            code=code,
            **kwargs,
        )
        response_body = self._client._request("POST", "/api/v1/otp/send", json=request.to_dict())
        return SendOtpResponse.from_dict(response_body)

    def verify(
        self,
        channel: str,
        code: str,
        recipient_phone: str | None = None,
        recipient_email: str | None = None,
        purpose: str = "login",
        **kwargs: Any,
    ) -> VerifyOtpResponse:
        request = VerifyOtpRequest(
            code=code,
            channel=VerifyOtpRequestChannel(channel),
            recipient_email=recipient_email,
            recipient_phone=recipient_phone,
            purpose=purpose,
            **kwargs,
        )
        response_body = self._client._request("POST", "/api/v1/otp/verify", json=request.to_dict())
        return VerifyOtpResponse.from_dict(response_body)
