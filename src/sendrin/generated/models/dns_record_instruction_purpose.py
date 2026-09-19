from enum import StrEnum


class DnsRecordInstructionPurpose(StrEnum):
    DKIM = "DKIM"
    DMARC = "DMARC"
    RETURN_PATH = "Return-Path"
    SPF = "SPF"

    def __str__(self) -> str:
        return str(self.value)
