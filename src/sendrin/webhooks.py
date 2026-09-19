from __future__ import annotations

import hashlib
import hmac
import time


class WebhookVerificationError(Exception):
    """Raised when a webhook's signature, timestamp, or format is invalid."""


def verify_webhook(
    *,
    body: bytes,
    timestamp: str,
    signature: str,
    secret: str,
    tolerance_seconds: int = 300,
) -> None:
    """Verify a Sendrin webhook delivery's HMAC-SHA256 signature.

    `body` MUST be the raw request body bytes exactly as received — do not
    parse and re-serialize the JSON before calling this function. Sendrin
    signs the exact bytes it transmits; re-serializing risks a whitespace or
    key-order mismatch that would make even a genuine, untampered webhook
    fail verification.

    Raises WebhookVerificationError if the signature is invalid, the
    signature format is unrecognized, or the timestamp is outside
    `tolerance_seconds` of the current time (replay-attack protection).
    """
    try:
        now = int(time.time())
        ts = int(timestamp)
    except (TypeError, ValueError) as exc:
        raise WebhookVerificationError(f"Invalid timestamp: {timestamp!r}") from exc

    if abs(now - ts) > tolerance_seconds:
        raise WebhookVerificationError(
            f"Timestamp {timestamp} is outside the {tolerance_seconds}s tolerance window "
            "(stale or replayed webhook)"
        )

    if not signature.startswith("v1="):
        raise WebhookVerificationError(f"Unrecognized signature format: {signature!r}")
    provided_sig = signature[len("v1=") :]

    expected_sig = hmac.new(
        secret.encode(), f"{timestamp}.".encode() + body, hashlib.sha256
    ).hexdigest()

    # Compare as bytes, not str: hmac.compare_digest raises TypeError when
    # given two `str` arguments and either contains non-ASCII characters.
    # `signature` comes straight from an untrusted request header, so a
    # malformed/malicious header must not escape as a raw TypeError — only
    # WebhookVerificationError is documented as raised by this function.
    if not hmac.compare_digest(provided_sig.encode(), expected_sig.encode()):
        raise WebhookVerificationError("Signature mismatch")
