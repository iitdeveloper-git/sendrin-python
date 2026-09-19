from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.application_branding import ApplicationBranding


T = TypeVar("T", bound="ApplicationRead")


@_attrs_define
class ApplicationRead:
    """
    Attributes:
        id (str):
        tenant_id (str):
        name (str):
        slug (str):
        status (str):
        default_locale (str):
        timezone (str):
        branding (ApplicationBranding):
        quota_per_minute (int):
        quota_per_day (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    tenant_id: str
    name: str
    slug: str
    status: str
    default_locale: str
    timezone: str
    branding: ApplicationBranding
    quota_per_minute: int
    quota_per_day: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        name = self.name

        slug = self.slug

        status = self.status

        default_locale = self.default_locale

        timezone = self.timezone

        branding = self.branding.to_dict()

        quota_per_minute = self.quota_per_minute

        quota_per_day = self.quota_per_day

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tenant_id": tenant_id,
                "name": name,
                "slug": slug,
                "status": status,
                "default_locale": default_locale,
                "timezone": timezone,
                "branding": branding,
                "quota_per_minute": quota_per_minute,
                "quota_per_day": quota_per_day,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_branding import ApplicationBranding  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenant_id")

        name = d.pop("name")

        slug = d.pop("slug")

        status = d.pop("status")

        default_locale = d.pop("default_locale")

        timezone = d.pop("timezone")

        branding = ApplicationBranding.from_dict(d.pop("branding"))

        quota_per_minute = d.pop("quota_per_minute")

        quota_per_day = d.pop("quota_per_day")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        application_read = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            slug=slug,
            status=status,
            default_locale=default_locale,
            timezone=timezone,
            branding=branding,
            quota_per_minute=quota_per_minute,
            quota_per_day=quota_per_day,
            created_at=created_at,
            updated_at=updated_at,
        )

        application_read.additional_properties = d
        return application_read

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
