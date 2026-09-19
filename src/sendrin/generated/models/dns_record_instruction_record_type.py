from enum import StrEnum


class DnsRecordInstructionRecordType(StrEnum):
    CNAME = "CNAME"
    MX = "MX"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
