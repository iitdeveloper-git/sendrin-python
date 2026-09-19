from enum import StrEnum


class EventCreateCompatibility(StrEnum):
    BACKWARD = "backward"
    FORWARD = "forward"
    FULL = "full"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
