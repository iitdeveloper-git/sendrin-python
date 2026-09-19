from __future__ import annotations


class SendrinAPIError(Exception):
    """Base exception raised for non-2xx responses from the Sendrin API.

    Attributes:
        status_code: The HTTP status code returned by the server (e.g. 400, 401, 500),
            or None if the error was caused by client-side or network failures.
        error_code: The structured error code returned in the response JSON payload
            (e.g., 'quota_exceeded', 'invalid_credentials', 'rate_limited'), or None.
    """

    def __init__(
        self, message: str, status_code: int | None = None, error_code: str | None = None
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


class SendrinQuotaExceededError(SendrinAPIError):
    """Exception raised when an API request fails due to exhausted tenant quotas (HTTP 429).

    This exception is deliberately NOT auto-retried by Sendrin._request to avoid wasting
    retries or burning additional balance against an exhausted quota limit.
    """
