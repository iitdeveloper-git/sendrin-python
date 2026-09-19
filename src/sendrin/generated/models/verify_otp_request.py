from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.verify_otp_request_channel import VerifyOtpRequestChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyOtpRequest")


@_attrs_define
class VerifyOtpRequest:
    """
    Attributes:
        code (str): OTP code entered by the user
        channel (VerifyOtpRequestChannel | Unset): Channel the OTP being verified was sent on. Default:
            VerifyOtpRequestChannel.EMAIL.
        recipient_email (None | str | Unset): Target email address being verified. Required for channel='email'.
        recipient_phone (None | str | Unset): Target phone number being verified, in E.164 format. Required for
            channel='sms'.
        purpose (str | Unset): Target verification purpose Default: 'login'.
    """

    code: str
    channel: VerifyOtpRequestChannel | Unset = VerifyOtpRequestChannel.EMAIL
    recipient_email: None | str | Unset = UNSET
    recipient_phone: None | str | Unset = UNSET
    purpose: str | Unset = "login"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        recipient_email: None | str | Unset
        if isinstance(self.recipient_email, Unset):
            recipient_email = UNSET
        else:
            recipient_email = self.recipient_email

        recipient_phone: None | str | Unset
        if isinstance(self.recipient_phone, Unset):
            recipient_phone = UNSET
        else:
            recipient_phone = self.recipient_phone

        purpose = self.purpose

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
        if recipient_phone is not UNSET:
            field_dict["recipient_phone"] = recipient_phone
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        _channel = d.pop("channel", UNSET)
        channel: VerifyOtpRequestChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = VerifyOtpRequestChannel(_channel)

        def _parse_recipient_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_email = _parse_recipient_email(d.pop("recipient_email", UNSET))

        def _parse_recipient_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_phone = _parse_recipient_phone(d.pop("recipient_phone", UNSET))

        purpose = d.pop("purpose", UNSET)

        verify_otp_request = cls(
            code=code,
            channel=channel,
            recipient_email=recipient_email,
            recipient_phone=recipient_phone,
            purpose=purpose,
        )

        verify_otp_request.additional_properties = d
        return verify_otp_request

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
