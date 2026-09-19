from enum import StrEnum


class InAppAckStatus(StrEnum):
    DELIVERED = "delivered"
    DISPLAYED = "displayed"
    OPENED = "opened"

    def __str__(self) -> str:
        return str(self.value)
