from enum import StrEnum


class ActivityListItemStatus(StrEnum):
    CANCELLED = "cancelled"
    DELIVERED = "delivered"
    EXPIRED = "expired"
    FAILED = "failed"
    PROCESSING = "processing"
    QUEUED = "queued"
    RETRYING = "retrying"
    SENT = "sent"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
