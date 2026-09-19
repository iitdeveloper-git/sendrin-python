import httpx
import pytest
from sendrin.client import Sendrin
from sendrin.exceptions import SendrinAPIError, SendrinQuotaExceededError


def _sendrin(handler, **kwargs) -> Sendrin:
    return Sendrin(api_key="gns_live_sk_test", transport=httpx.MockTransport(handler), **kwargs)


def test_otp_send_success_reaches_right_path_with_auth_header():
    captured: dict[str, httpx.Request] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(
            200,
            json={
                "otp_id": "otp_123",
                "channel": "sms",
                "expires_at": "2026-09-19T12:00:00+00:00",
                "ttl_seconds": 600,
                "purpose": "login",
                "remaining_credits": 42,
                "status": "sent",
            },
        )

    client = _sendrin(handler)
    result = client.otp.send(channel="sms", recipient_phone="+14155552671", purpose="login")

    request = captured["request"]
    assert request.method == "POST"
    assert request.url.path == "/api/v1/otp/send"
    assert request.headers["Authorization"] == "Bearer gns_live_sk_test"
    assert result.otp_id == "otp_123"
    assert result.remaining_credits == 42


def test_otp_send_429_raises_quota_exceeded_without_retry():
    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        call_count += 1
        return httpx.Response(
            429, json={"detail": {"message": "Quota exceeded", "code": "quota_exceeded"}}
        )

    client = _sendrin(handler, max_retries=2)

    with pytest.raises(SendrinQuotaExceededError) as exc_info:
        client.otp.send(channel="sms", recipient_phone="+14155552671")

    assert exc_info.value.status_code == 429
    # 429 must not be retried — a single attempt only.
    assert call_count == 1


def test_otp_send_500_retries_up_to_max_retries_then_raises_api_error():
    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        call_count += 1
        return httpx.Response(500, json={"detail": {"message": "Internal error"}})

    client = _sendrin(handler, max_retries=2)

    with pytest.raises(SendrinAPIError) as exc_info:
        client.otp.send(channel="sms", recipient_phone="+14155552671")

    assert exc_info.value.status_code == 500
    # Initial attempt + max_retries retries.
    assert call_count == 3


def test_otp_send_network_error_retries_with_backoff(monkeypatch):
    sleeps: list[float] = []
    monkeypatch.setattr("sendrin.client.time.sleep", lambda seconds: sleeps.append(seconds))

    call_count = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal call_count
        call_count += 1
        raise httpx.ConnectError("connection refused", request=request)

    client = _sendrin(handler, max_retries=2)

    with pytest.raises(SendrinAPIError):
        client.otp.send(channel="sms", recipient_phone="+14155552671")

    assert call_count == 3
    assert sleeps == [0.5, 1.0]


def test_otp_verify_success():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/otp/verify"
        return httpx.Response(
            200,
            json={"verified": True, "message": "OTP verified", "remaining_attempts": 2},
        )

    client = _sendrin(handler)
    result = client.otp.verify(channel="sms", code="123456", recipient_phone="+14155552671")

    assert result.verified is True
    assert result.remaining_attempts == 2
