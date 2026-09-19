from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyOtpResponse")


@_attrs_define
class VerifyOtpResponse:
    """
    Attributes:
        verified (bool): Whether the OTP was successfully validated
        message (str): Human-readable result status
        verification_token (None | str | Unset): One-time signed token proving verification success
        verified_at (datetime.datetime | None | Unset): UTC timestamp of successful verification
        remaining_attempts (int | None | Unset): Remaining tries before OTP is invalidated
    """

    verified: bool
    message: str
    verification_token: None | str | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    remaining_attempts: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verified = self.verified

        message = self.message

        verification_token: None | str | Unset
        if isinstance(self.verification_token, Unset):
            verification_token = UNSET
        else:
            verification_token = self.verification_token

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        remaining_attempts: int | None | Unset
        if isinstance(self.remaining_attempts, Unset):
            remaining_attempts = UNSET
        else:
            remaining_attempts = self.remaining_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verified": verified,
                "message": message,
            }
        )
        if verification_token is not UNSET:
            field_dict["verification_token"] = verification_token
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if remaining_attempts is not UNSET:
            field_dict["remaining_attempts"] = remaining_attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verified = d.pop("verified")

        message = d.pop("message")

        def _parse_verification_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_token = _parse_verification_token(d.pop("verification_token", UNSET))

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        def _parse_remaining_attempts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        remaining_attempts = _parse_remaining_attempts(d.pop("remaining_attempts", UNSET))

        verify_otp_response = cls(
            verified=verified,
            message=message,
            verification_token=verification_token,
            verified_at=verified_at,
            remaining_attempts=remaining_attempts,
        )

        verify_otp_response.additional_properties = d
        return verify_otp_response

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
