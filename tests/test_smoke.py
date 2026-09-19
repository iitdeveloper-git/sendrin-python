"""Smoke tests proving the generated low-level client is importable and usable.

These do not hit the network -- they only confirm that codegen output
(sendrin.generated) is structurally sound: the client classes construct,
carry the configured base URL, and at least one real generated endpoint
module (derived from apps/docs/content/openapi.json) is importable and
exposes the expected callables.
"""

import httpx


def test_generated_client_importable_and_constructs():
    from sendrin.generated import AuthenticatedClient, Client

    client = Client(base_url="https://api.sendrin.com")
    assert client is not None
    assert client.get_httpx_client().base_url == httpx.URL("https://api.sendrin.com")

    fake_token = "not-a-real-token"  # noqa: S105 -- test fixture value, not a secret
    auth_client = AuthenticatedClient(base_url="https://api.sendrin.com", token=fake_token)  # noqa: S106
    assert auth_client.token == fake_token
    # AuthenticatedClient injects a bearer Authorization header derived from the token.
    assert auth_client.get_httpx_client().headers["Authorization"] == f"Bearer {fake_token}"


def test_generated_endpoint_module_is_real():
    """Exercise a real generated endpoint (OTP send) to prove codegen produced
    actual API bindings, not just the bare client shell."""
    from sendrin.generated.api.otp import send_otp_api_v1_otp_send_post as send_otp
    from sendrin.generated.models.send_otp_request import SendOtpRequest
    from sendrin.generated.models.send_otp_request_channel import SendOtpRequestChannel

    assert callable(send_otp.sync)
    assert callable(send_otp.asyncio)
    # The generated request model should round-trip through its own (de)serializer.
    payload = SendOtpRequest.from_dict({"channel": "sms", "recipient_phone": "+15551234567"})
    assert payload.channel is SendOtpRequestChannel.SMS
    assert payload.to_dict()["recipient_phone"] == "+15551234567"
