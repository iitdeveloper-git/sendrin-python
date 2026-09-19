from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_otp_response_channel import SendOtpResponseChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendOtpResponse")


@_attrs_define
class SendOtpResponse:
    """
    Attributes:
        otp_id (str): Unique tracking identifier for this OTP request
        channel (SendOtpResponseChannel): Channel the OTP was dispatched on
        expires_at (datetime.datetime): UTC expiration timestamp
        ttl_seconds (int): Remaining validity in seconds
        purpose (str): Target verification purpose
        remaining_credits (int): Remaining tenant OTP credit balance
        status (Literal['sent'] | Unset):  Default: 'sent'.
    """

    otp_id: str
    channel: SendOtpResponseChannel
    expires_at: datetime.datetime
    ttl_seconds: int
    purpose: str
    remaining_credits: int
    status: Literal["sent"] | Unset = "sent"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        otp_id = self.otp_id

        channel = self.channel.value

        expires_at = self.expires_at.isoformat()

        ttl_seconds = self.ttl_seconds

        purpose = self.purpose

        remaining_credits = self.remaining_credits

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "otp_id": otp_id,
                "channel": channel,
                "expires_at": expires_at,
                "ttl_seconds": ttl_seconds,
                "purpose": purpose,
                "remaining_credits": remaining_credits,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        otp_id = d.pop("otp_id")

        channel = SendOtpResponseChannel(d.pop("channel"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        ttl_seconds = d.pop("ttl_seconds")

        purpose = d.pop("purpose")

        remaining_credits = d.pop("remaining_credits")

        status = cast(Literal["sent"] | Unset, d.pop("status", UNSET))
        if status != "sent" and not isinstance(status, Unset):
            raise ValueError(f"status must match const 'sent', got '{status}'")

        send_otp_response = cls(
            otp_id=otp_id,
            channel=channel,
            expires_at=expires_at,
            ttl_seconds=ttl_seconds,
            purpose=purpose,
            remaining_credits=remaining_credits,
            status=status,
        )

        send_otp_response.additional_properties = d
        return send_otp_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
