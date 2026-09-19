from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_branding import ApplicationBranding


T = TypeVar("T", bound="ApplicationUpdate")


@_attrs_define
class ApplicationUpdate:
    """
    Attributes:
        name (None | str | Unset):
        default_locale (None | str | Unset):
        timezone (None | str | Unset):
        branding (ApplicationBranding | None | Unset):
        quota_per_minute (int | None | Unset):
        quota_per_day (int | None | Unset):
    """

    name: None | str | Unset = UNSET
    default_locale: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    branding: ApplicationBranding | None | Unset = UNSET
    quota_per_minute: int | None | Unset = UNSET
    quota_per_day: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.application_branding import ApplicationBranding  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        default_locale: None | str | Unset
        if isinstance(self.default_locale, Unset):
            default_locale = UNSET
        else:
            default_locale = self.default_locale

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        branding: dict[str, Any] | None | Unset
        if isinstance(self.branding, Unset):
            branding = UNSET
        elif isinstance(self.branding, ApplicationBranding):
            branding = self.branding.to_dict()
        else:
            branding = self.branding

        quota_per_minute: int | None | Unset
        if isinstance(self.quota_per_minute, Unset):
            quota_per_minute = UNSET
        else:
            quota_per_minute = self.quota_per_minute

        quota_per_day: int | None | Unset
        if isinstance(self.quota_per_day, Unset):
            quota_per_day = UNSET
        else:
            quota_per_day = self.quota_per_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_default_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_locale = _parse_default_locale(d.pop("default_locale", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_branding(data: object) -> ApplicationBranding | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                branding_type_0 = ApplicationBranding.from_dict(data)

                return branding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApplicationBranding | None | Unset, data)

        branding = _parse_branding(d.pop("branding", UNSET))

        def _parse_quota_per_minute(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_per_minute = _parse_quota_per_minute(d.pop("quota_per_minute", UNSET))

        def _parse_quota_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        quota_per_day = _parse_quota_per_day(d.pop("quota_per_day", UNSET))

        application_update = cls(
            name=name,
            default_locale=default_locale,
            timezone=timezone,
            branding=branding,
            quota_per_minute=quota_per_minute,
            quota_per_day=quota_per_day,
        )

        application_update.additional_properties = d
        return application_update

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
