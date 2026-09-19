from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_branding import ApplicationBranding


T = TypeVar("T", bound="ApplicationCreate")


@_attrs_define
class ApplicationCreate:
    """
    Attributes:
        name (str):
        slug (str):
        default_locale (str | Unset):  Default: 'en'.
        timezone (str | Unset):  Default: 'UTC'.
        branding (ApplicationBranding | Unset):
        quota_per_minute (int | Unset):  Default: 60.
        quota_per_day (int | Unset):  Default: 10000.
    """

    name: str
    slug: str
    default_locale: str | Unset = "en"
    timezone: str | Unset = "UTC"
    branding: ApplicationBranding | Unset = UNSET
    quota_per_minute: int | Unset = 60
    quota_per_day: int | Unset = 10000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        default_locale = self.default_locale

        timezone = self.timezone

        branding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branding, Unset):
            branding = self.branding.to_dict()

        quota_per_minute = self.quota_per_minute

        quota_per_day = self.quota_per_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
            }
        )
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if branding is not UNSET:
            field_dict["branding"] = branding
        if quota_per_minute is not UNSET:
            field_dict["quota_per_minute"] = quota_per_minute
        if quota_per_day is not UNSET:
            field_dict["quota_per_day"] = quota_per_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_branding import ApplicationBranding  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        slug = d.pop("slug")

        default_locale = d.pop("default_locale", UNSET)

        timezone = d.pop("timezone", UNSET)

        _branding = d.pop("branding", UNSET)
        branding: ApplicationBranding | Unset
        if isinstance(_branding, Unset):
            branding = UNSET
        else:
            branding = ApplicationBranding.from_dict(_branding)

        quota_per_minute = d.pop("quota_per_minute", UNSET)

        quota_per_day = d.pop("quota_per_day", UNSET)

        application_create = cls(
            name=name,
            slug=slug,
            default_locale=default_locale,
            timezone=timezone,
            branding=branding,
            quota_per_minute=quota_per_minute,
            quota_per_day=quota_per_day,
        )

        application_create.additional_properties = d
        return application_create

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
