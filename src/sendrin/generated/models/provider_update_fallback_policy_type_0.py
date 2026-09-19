from enum import StrEnum


class ProviderUpdateFallbackPolicyType0(StrEnum):
    DEFAULT_IF_ABSENT = "default_if_absent"
    EXPLICIT_FAILOVER = "explicit_failover"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
