from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_read_branding import TenantReadBranding


T = TypeVar("T", bound="TenantRead")


@_attrs_define
class TenantRead:
    """
    Attributes:
        id (str):
        name (str):
        slug (str):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        branding (TenantReadBranding | Unset):
    """

    id: str
    name: str
    slug: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    branding: TenantReadBranding | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        branding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if branding is not UNSET:
            field_dict["branding"] = branding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_read_branding import TenantReadBranding  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _branding = d.pop("branding", UNSET)
        branding: TenantReadBranding | Unset
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = TenantReadBranding.from_dict(_branding)

        tenant_read = cls(
            id=id,
            name=name,
            slug=slug,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            branding=branding,
        )

        tenant_read.additional_properties = d
        return tenant_read

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
