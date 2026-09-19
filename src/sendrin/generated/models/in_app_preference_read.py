from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.in_app_preference_read_quiet_hours import InAppPreferenceReadQuietHours


T = TypeVar("T", bound="InAppPreferenceRead")


@_attrs_define
class InAppPreferenceRead:
    """
    Attributes:
        user_id (str):
        event_key (str):
        in_app_enabled (bool):
        toast_enabled (bool):
        sound_enabled (bool):
        quiet_hours (InAppPreferenceReadQuietHours):
        minimum_priority (int):
    """

    user_id: str
    event_key: str
    in_app_enabled: bool
    toast_enabled: bool
    sound_enabled: bool
    quiet_hours: InAppPreferenceReadQuietHours
    minimum_priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        event_key = self.event_key

        in_app_enabled = self.in_app_enabled

        toast_enabled = self.toast_enabled

        sound_enabled = self.sound_enabled

        quiet_hours = self.quiet_hours.to_dict()

        minimum_priority = self.minimum_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "event_key": event_key,
                "in_app_enabled": in_app_enabled,
                "toast_enabled": toast_enabled,
                "sound_enabled": sound_enabled,
                "quiet_hours": quiet_hours,
                "minimum_priority": minimum_priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_app_preference_read_quiet_hours import (
            InAppPreferenceReadQuietHours,  # noqa: PLC0415
        )

        d = dict(src_dict)
        user_id = d.pop("user_id")

        event_key = d.pop("event_key")

        in_app_enabled = d.pop("in_app_enabled")

        toast_enabled = d.pop("toast_enabled")

        sound_enabled = d.pop("sound_enabled")

        quiet_hours = InAppPreferenceReadQuietHours.from_dict(d.pop("quiet_hours"))

        minimum_priority = d.pop("minimum_priority")

        in_app_preference_read = cls(
            user_id=user_id,
            event_key=event_key,
            in_app_enabled=in_app_enabled,
            toast_enabled=toast_enabled,
            sound_enabled=sound_enabled,
            quiet_hours=quiet_hours,
            minimum_priority=minimum_priority,
        )

        in_app_preference_read.additional_properties = d
        return in_app_preference_read

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
