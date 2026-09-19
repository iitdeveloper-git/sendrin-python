from enum import StrEnum


class ProviderCreateFallbackPolicy(StrEnum):
    DEFAULT_IF_ABSENT = "default_if_absent"
    EXPLICIT_FAILOVER = "explicit_failover"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
