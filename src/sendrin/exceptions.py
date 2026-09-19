from __future__ import annotations


class SendrinAPIError(Exception):
    def __init__(
        self, message: str, status_code: int | None = None, error_code: str | None = None
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


class SendrinQuotaExceededError(SendrinAPIError):
    """429 quota_exceeded — deliberately not auto-retried, see Sendrin._request."""
