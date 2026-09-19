from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainVerifyResponse")


@_attrs_define
class DomainVerifyResponse:
    """
    Attributes:
        id (str):
        name (str):
        status (str):
        dkim_status (str):
        spf_status (str):
        return_path_status (str):
        dmarc_status (str):
        is_active (bool):
        checked_at (datetime.datetime):
        verification_error (None | str | Unset):
    """

    id: str
    name: str
    status: str
    dkim_status: str
    spf_status: str
    return_path_status: str
    dmarc_status: str
    is_active: bool
    checked_at: datetime.datetime
    verification_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        dkim_status = self.dkim_status

        spf_status = self.spf_status

        return_path_status = self.return_path_status

        dmarc_status = self.dmarc_status

        is_active = self.is_active

        checked_at = self.checked_at.isoformat()

        verification_error: None | str | Unset
        if isinstance(self.verification_error, Unset):
            verification_error = UNSET
        else:
            verification_error = self.verification_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "dkim_status": dkim_status,
                "spf_status": spf_status,
                "return_path_status": return_path_status,
                "dmarc_status": dmarc_status,
                "is_active": is_active,
                "checked_at": checked_at,
            }
        )
        if verification_error is not UNSET:
            field_dict["verification_error"] = verification_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        dkim_status = d.pop("dkim_status")

        spf_status = d.pop("spf_status")

        return_path_status = d.pop("return_path_status")

        dmarc_status = d.pop("dmarc_status")

        is_active = d.pop("is_active")

        checked_at = datetime.datetime.fromisoformat(d.pop("checked_at"))

        def _parse_verification_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_error = _parse_verification_error(d.pop("verification_error", UNSET))

        domain_verify_response = cls(
            id=id,
            name=name,
            status=status,
            dkim_status=dkim_status,
            spf_status=spf_status,
            return_path_status=return_path_status,
            dmarc_status=dmarc_status,
            is_active=is_active,
            checked_at=checked_at,
            verification_error=verification_error,
        )

        domain_verify_response.additional_properties = d
        return domain_verify_response

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
