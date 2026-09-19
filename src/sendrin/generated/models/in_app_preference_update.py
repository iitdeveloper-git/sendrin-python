from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_app_preference_update_quiet_hours_type_0 import (
        InAppPreferenceUpdateQuietHoursType0,
    )


T = TypeVar("T", bound="InAppPreferenceUpdate")


@_attrs_define
class InAppPreferenceUpdate:
    """
    Attributes:
        event_key (str | Unset):  Default: '*'.
        in_app_enabled (bool | None | Unset):
        toast_enabled (bool | None | Unset):
        sound_enabled (bool | None | Unset):
        quiet_hours (InAppPreferenceUpdateQuietHoursType0 | None | Unset):
        minimum_priority (int | None | Unset):
    """

    event_key: str | Unset = "*"
    in_app_enabled: bool | None | Unset = UNSET
    toast_enabled: bool | None | Unset = UNSET
    sound_enabled: bool | None | Unset = UNSET
    quiet_hours: InAppPreferenceUpdateQuietHoursType0 | None | Unset = UNSET
    minimum_priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.in_app_preference_update_quiet_hours_type_0 import (
            InAppPreferenceUpdateQuietHoursType0,  # noqa: PLC0415
        )

        event_key = self.event_key

        in_app_enabled: bool | None | Unset
        if isinstance(self.in_app_enabled, Unset):
            in_app_enabled = UNSET
        else:
            in_app_enabled = self.in_app_enabled

        toast_enabled: bool | None | Unset
        if isinstance(self.toast_enabled, Unset):
            toast_enabled = UNSET
        else:
            toast_enabled = self.toast_enabled

        sound_enabled: bool | None | Unset
        if isinstance(self.sound_enabled, Unset):
            sound_enabled = UNSET
        else:
            sound_enabled = self.sound_enabled

        quiet_hours: dict[str, Any] | None | Unset
        if isinstance(self.quiet_hours, Unset):
            quiet_hours = UNSET
        elif isinstance(self.quiet_hours, InAppPreferenceUpdateQuietHoursType0):
            quiet_hours = self.quiet_hours.to_dict()
        else:
            quiet_hours = self.quiet_hours

        minimum_priority: int | None | Unset
        if isinstance(self.minimum_priority, Unset):
            minimum_priority = UNSET
        else:
            minimum_priority = self.minimum_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_key is not UNSET:
            field_dict["event_key"] = event_key
        if in_app_enabled is not UNSET:
            field_dict["in_app_enabled"] = in_app_enabled
        if toast_enabled is not UNSET:
            field_dict["toast_enabled"] = toast_enabled
        if sound_enabled is not UNSET:
            field_dict["sound_enabled"] = sound_enabled
        if quiet_hours is not UNSET:
            field_dict["quiet_hours"] = quiet_hours
        if minimum_priority is not UNSET:
            field_dict["minimum_priority"] = minimum_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_app_preference_update_quiet_hours_type_0 import (
            InAppPreferenceUpdateQuietHoursType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        event_key = d.pop("event_key", UNSET)

        def _parse_in_app_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        in_app_enabled = _parse_in_app_enabled(d.pop("in_app_enabled", UNSET))

        def _parse_toast_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        toast_enabled = _parse_toast_enabled(d.pop("toast_enabled", UNSET))

        def _parse_sound_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sound_enabled = _parse_sound_enabled(d.pop("sound_enabled", UNSET))

        def _parse_quiet_hours(data: object) -> InAppPreferenceUpdateQuietHoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quiet_hours_type_0 = InAppPreferenceUpdateQuietHoursType0.from_dict(data)

                return quiet_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InAppPreferenceUpdateQuietHoursType0 | None | Unset, data)

        quiet_hours = _parse_quiet_hours(d.pop("quiet_hours", UNSET))

        def _parse_minimum_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minimum_priority = _parse_minimum_priority(d.pop("minimum_priority", UNSET))

        in_app_preference_update = cls(
            event_key=event_key,
            in_app_enabled=in_app_enabled,
            toast_enabled=toast_enabled,
            sound_enabled=sound_enabled,
            quiet_hours=quiet_hours,
            minimum_priority=minimum_priority,
        )

        in_app_preference_update.additional_properties = d
        return in_app_preference_update

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
