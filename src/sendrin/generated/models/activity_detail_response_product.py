from enum import StrEnum


class ActivityDetailResponseProduct(StrEnum):
    NOTIFICATION = "notification"
    OTP = "otp"

    def __str__(self) -> str:
        return str(self.value)
