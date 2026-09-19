from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_timeline_entry_status import ActivityTimelineEntryStatus

T = TypeVar("T", bound="ActivityTimelineEntry")


@_attrs_define
class ActivityTimelineEntry:
    """
    Attributes:
        label (str):
        occurred_at (datetime.datetime | None):
        status (ActivityTimelineEntryStatus):
    """

    label: str
    occurred_at: datetime.datetime | None
    status: ActivityTimelineEntryStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        occurred_at: None | str
        if isinstance(self.occurred_at, datetime.datetime):
            occurred_at = self.occurred_at.isoformat()
        else:
            occurred_at = self.occurred_at

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "occurred_at": occurred_at,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_occurred_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                occurred_at_type_0 = datetime.datetime.fromisoformat(data)

                return occurred_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        occurred_at = _parse_occurred_at(d.pop("occurred_at"))

        status = ActivityTimelineEntryStatus(d.pop("status"))

        activity_timeline_entry = cls(
            label=label,
            occurred_at=occurred_at,
            status=status,
        )

        activity_timeline_entry.additional_properties = d
        return activity_timeline_entry

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
