from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivitySummaryResponse")


@_attrs_define
class ActivitySummaryResponse:
    """
    Attributes:
        total (int):
        delivered (int):
        delivered_pct (float):
        failed (int):
        failed_pct (float):
        in_progress (int):
        in_progress_pct (float):
    """

    total: int
    delivered: int
    delivered_pct: float
    failed: int
    failed_pct: float
    in_progress: int
    in_progress_pct: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        delivered = self.delivered

        delivered_pct = self.delivered_pct

        failed = self.failed

        failed_pct = self.failed_pct

        in_progress = self.in_progress

        in_progress_pct = self.in_progress_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "delivered": delivered,
                "delivered_pct": delivered_pct,
                "failed": failed,
                "failed_pct": failed_pct,
                "in_progress": in_progress,
                "in_progress_pct": in_progress_pct,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        delivered = d.pop("delivered")

        delivered_pct = d.pop("delivered_pct")

        failed = d.pop("failed")

        failed_pct = d.pop("failed_pct")

        in_progress = d.pop("in_progress")

        in_progress_pct = d.pop("in_progress_pct")

        activity_summary_response = cls(
            total=total,
            delivered=delivered,
            delivered_pct=delivered_pct,
            failed=failed,
            failed_pct=failed_pct,
            in_progress=in_progress,
            in_progress_pct=in_progress_pct,
        )

        activity_summary_response.additional_properties = d
        return activity_summary_response

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
