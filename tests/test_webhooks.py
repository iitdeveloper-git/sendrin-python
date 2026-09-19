import hashlib
import hmac
import time

import pytest
from sendrin.webhooks import WebhookVerificationError, verify_webhook


def _sign(secret: str, timestamp: str, body: bytes) -> str:
    sig = hmac.new(secret.encode(), f"{timestamp}.".encode() + body, hashlib.sha256).hexdigest()
    return f"v1={sig}"


def test_verify_webhook_accepts_valid_signature():
    secret = "whsec_test_12345"  # noqa: S105 -- test fixture value, not a secret
    body = b'{"event":"notification.delivered","id":"ntf_abc"}'
    timestamp = str(int(time.time()))
    signature = _sign(secret, timestamp, body)

    # Must not raise.
    verify_webhook(body=body, timestamp=timestamp, signature=signature, secret=secret)


def test_verify_webhook_rejects_tampered_body():
    secret = "whsec_test_12345"  # noqa: S105 -- test fixture value, not a secret
    body = b'{"event":"notification.delivered","id":"ntf_abc"}'
    timestamp = str(int(time.time()))
    signature = _sign(secret, timestamp, body)
    tampered_body = b'{"event":"notification.delivered","id":"ntf_XXX"}'

    with pytest.raises(WebhookVerificationError):
        verify_webhook(body=tampered_body, timestamp=timestamp, signature=signature, secret=secret)


def test_verify_webhook_rejects_wrong_secret():
    body = b'{"event":"notification.delivered","id":"ntf_abc"}'
    timestamp = str(int(time.time()))
    signature = _sign("whsec_test_12345", timestamp, body)

    with pytest.raises(WebhookVerificationError):
        verify_webhook(
            body=body,
            timestamp=timestamp,
            signature=signature,
            secret="whsec_wrong",  # noqa: S106 -- test fixture value, not a secret
        )


def test_verify_webhook_rejects_stale_timestamp():
    secret = "whsec_test_12345"  # noqa: S105 -- test fixture value, not a secret
    body = b'{"event":"notification.delivered","id":"ntf_abc"}'
    old_timestamp = str(int(time.time()) - 3600)  # 1 hour old
    signature = _sign(secret, old_timestamp, body)

    with pytest.raises(WebhookVerificationError, match="stale|expired|tolerance"):
        verify_webhook(body=body, timestamp=old_timestamp, signature=signature, secret=secret)


def test_verify_webhook_non_ascii_signature_raises_verification_error_not_type_error():
    """hmac.compare_digest raises TypeError when comparing two `str` values
    where one contains non-ASCII characters. `signature` comes straight from
    an untrusted request header, so a malformed/malicious header must surface
    as the documented WebhookVerificationError, never a raw TypeError."""
    secret = "whsec_test_12345"  # noqa: S105 -- test fixture value, not a secret
    body = b'{"event":"notification.delivered","id":"ntf_abc"}'
    timestamp = str(int(time.time()))
    signature = "v1=" + "ü" * 64

    with pytest.raises(WebhookVerificationError):
        verify_webhook(body=body, timestamp=timestamp, signature=signature, secret=secret)


def test_verify_webhook_does_not_reserialize_json():
    """The critical correctness case from this plan's Spec section: verification
    must work against raw bytes with non-canonical formatting (extra whitespace,
    different key order) as long as the bytes match what was actually signed —
    proving the implementation doesn't round-trip through json.loads/json.dumps
    before verifying, which would break on exactly this kind of real-world input."""
    secret = "whsec_test_12345"  # noqa: S105 -- test fixture value, not a secret
    # Deliberately non-compact, non-sorted-key JSON bytes — if verify_webhook
    # re-serializes before hashing, this test fails even though the signature
    # over these EXACT bytes is correct.
    body = b'{"id": "ntf_abc", "event": "notification.delivered"}'
    timestamp = str(int(time.time()))
    signature = _sign(secret, timestamp, body)

    verify_webhook(body=body, timestamp=timestamp, signature=signature, secret=secret)
