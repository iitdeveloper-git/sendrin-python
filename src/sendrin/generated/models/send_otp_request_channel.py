from enum import StrEnum


class SendOtpRequestChannel(StrEnum):
    EMAIL = "email"
    SMS = "sms"

    def __str__(self) -> str:
        return str(self.value)
