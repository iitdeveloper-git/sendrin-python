from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_read_recipient_policy import EventReadRecipientPolicy


T = TypeVar("T", bound="EventRead")


@_attrs_define
class EventRead:
    """
    Attributes:
        id (str):
        application_id (str):
        event_key (str):
        status (str):
        allowed_channels (list[str]):
        recipient_policy (EventReadRecipientPolicy):
        current_schema_version (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    application_id: str
    event_key: str
    status: str
    allowed_channels: list[str]
    recipient_policy: EventReadRecipientPolicy
    current_schema_version: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        application_id = self.application_id

        event_key = self.event_key

        status = self.status

        allowed_channels = self.allowed_channels

        recipient_policy = self.recipient_policy.to_dict()

        current_schema_version = self.current_schema_version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "application_id": application_id,
                "event_key": event_key,
                "status": status,
                "allowed_channels": allowed_channels,
                "recipient_policy": recipient_policy,
                "current_schema_version": current_schema_version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_read_recipient_policy import EventReadRecipientPolicy  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        application_id = d.pop("application_id")

        event_key = d.pop("event_key")

        status = d.pop("status")

        allowed_channels = cast(list[str], d.pop("allowed_channels"))

        recipient_policy = EventReadRecipientPolicy.from_dict(d.pop("recipient_policy"))

        current_schema_version = d.pop("current_schema_version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        event_read = cls(
            id=id,
            application_id=application_id,
            event_key=event_key,
            status=status,
            allowed_channels=allowed_channels,
            recipient_policy=recipient_policy,
            current_schema_version=current_schema_version,
            created_at=created_at,
            updated_at=updated_at,
        )

        event_read.additional_properties = d
        return event_read

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
