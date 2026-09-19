from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_otp_request_channel import SendOtpRequestChannel
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendOtpRequest")


@_attrs_define
class SendOtpRequest:
    """
    Attributes:
        channel (SendOtpRequestChannel | Unset): Delivery channel for the OTP code: 'email' or 'sms'. Default:
            SendOtpRequestChannel.EMAIL.
        recipient_email (None | str | Unset): Target email address. Required when channel='email'.
        recipient_phone (None | str | Unset): Target phone number in E.164 format (e.g. +14155552671). Required when
            channel='sms'.
        purpose (str | Unset): Reason for OTP (e.g. login, signup, verification, password_reset, transaction) Default:
            'login'.
        code_length (int | Unset): Length of the randomly generated OTP code (4, 6, or 8 digits). Ignored if 'code' is
            provided. Default: 6.
        ttl_seconds (int | Unset): Expiration time in seconds (default: 600s / 10 minutes) Default: 600.
        brand_name (None | str | Unset): Optional brand override. If omitted, auto-resolves from the caller's
            Application.branding record; falls back to 'IITDeveloper' if neither is set.
        application_id (None | str | Unset): Application to auto-resolve branding from. Usually inferred from the
            authenticated API key's principal; only needed here to override that.
        support_email (None | str | Unset): Support contact email displayed in footer
        code (None | str | Unset): Optional client-supplied OTP code (4-16 alphanumeric, hyphens, underscores). If
            provided, GNS skips random generation and delivers/verifies this code directly.
    """

    channel: SendOtpRequestChannel | Unset = SendOtpRequestChannel.EMAIL
    recipient_email: None | str | Unset = UNSET
    recipient_phone: None | str | Unset = UNSET
    purpose: str | Unset = "login"
    code_length: int | Unset = 6
    ttl_seconds: int | Unset = 600
    brand_name: None | str | Unset = UNSET
    application_id: None | str | Unset = UNSET
    support_email: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        code_length = self.code_length

        ttl_seconds = self.ttl_seconds

        brand_name: None | str | Unset
        if isinstance(self.brand_name, Unset):
            brand_name = UNSET
        else:
            brand_name = self.brand_name

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        else:
            application_id = self.application_id

        support_email: None | str | Unset
        if isinstance(self.support_email, Unset):
            support_email = UNSET
        else:
            support_email = self.support_email

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if recipient_email is not UNSET:
            field_dict["recipient_email"] = recipient_email
        if recipient_phone is not UNSET:
            field_dict["recipient_phone"] = recipient_phone
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if code_length is not UNSET:
            field_dict["code_length"] = code_length
        if ttl_seconds is not UNSET:
            field_dict["ttl_seconds"] = ttl_seconds
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channel = d.pop("channel", UNSET)
        channel: SendOtpRequestChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = SendOtpRequestChannel(_channel)

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

        code_length = d.pop("code_length", UNSET)

        ttl_seconds = d.pop("ttl_seconds", UNSET)

        def _parse_brand_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand_name = _parse_brand_name(d.pop("brand_name", UNSET))

        def _parse_application_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_id = _parse_application_id(d.pop("application_id", UNSET))

        def _parse_support_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_email = _parse_support_email(d.pop("support_email", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        send_otp_request = cls(
            channel=channel,
            recipient_email=recipient_email,
            recipient_phone=recipient_phone,
            purpose=purpose,
            code_length=code_length,
            ttl_seconds=ttl_seconds,
            brand_name=brand_name,
            application_id=application_id,
            support_email=support_email,
            code=code,
        )

        send_otp_request.additional_properties = d
        return send_otp_request

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
