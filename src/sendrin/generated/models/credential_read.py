from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CredentialRead")


@_attrs_define
class CredentialRead:
    """
    Attributes:
        id (str):
        application_id (str):
        name (str):
        key_prefix (str):
        permissions (list[str]):
        expires_at (datetime.datetime | None):
        last_used_at (datetime.datetime | None):
        revoked_at (datetime.datetime | None):
        overlap_ends_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: str
    application_id: str
    name: str
    key_prefix: str
    permissions: list[str]
    expires_at: datetime.datetime | None
    last_used_at: datetime.datetime | None
    revoked_at: datetime.datetime | None
    overlap_ends_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        application_id = self.application_id

        name = self.name

        key_prefix = self.key_prefix

        permissions = self.permissions

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        revoked_at: None | str
        if isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        overlap_ends_at: None | str
        if isinstance(self.overlap_ends_at, datetime.datetime):
            overlap_ends_at = self.overlap_ends_at.isoformat()
        else:
            overlap_ends_at = self.overlap_ends_at

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "application_id": application_id,
                "name": name,
                "key_prefix": key_prefix,
                "permissions": permissions,
                "expires_at": expires_at,
                "last_used_at": last_used_at,
                "revoked_at": revoked_at,
                "overlap_ends_at": overlap_ends_at,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        application_id = d.pop("application_id")

        name = d.pop("name")

        key_prefix = d.pop("key_prefix")

        permissions = cast(list[str], d.pop("permissions"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        def _parse_revoked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))

        def _parse_overlap_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                overlap_ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return overlap_ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        overlap_ends_at = _parse_overlap_ends_at(d.pop("overlap_ends_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        credential_read = cls(
            id=id,
            application_id=application_id,
            name=name,
            key_prefix=key_prefix,
            permissions=permissions,
            expires_at=expires_at,
            last_used_at=last_used_at,
            revoked_at=revoked_at,
            overlap_ends_at=overlap_ends_at,
            created_at=created_at,
        )

        credential_read.additional_properties = d
        return credential_read

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
