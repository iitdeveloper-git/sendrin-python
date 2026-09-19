from enum import StrEnum


class ProviderConnectionTestChannel(StrEnum):
    EMAIL = "email"
    IN_APP = "in_app"
    PUSH = "push"
    SMS = "sms"
    TELEGRAM = "telegram"
    WEBHOOK = "webhook"
    WHATSAPP = "whatsapp"

    def __str__(self) -> str:
        return str(self.value)
