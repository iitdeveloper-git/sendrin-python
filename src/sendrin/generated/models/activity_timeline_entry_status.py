from enum import StrEnum


class ActivityTimelineEntryStatus(StrEnum):
    COMPLETE = "complete"
    CURRENT = "current"
    FAILED = "failed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
