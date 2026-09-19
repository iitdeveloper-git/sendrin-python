from enum import StrEnum


class DnsRecordInstructionStatus(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
