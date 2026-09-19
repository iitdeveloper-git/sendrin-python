from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_create_allowed_channels_item import EventCreateAllowedChannelsItem
from ..models.event_create_compatibility import EventCreateCompatibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_create_recipient_policy import EventCreateRecipientPolicy
    from ..models.event_create_schema import EventCreateSchema


T = TypeVar("T", bound="EventCreate")


@_attrs_define
class EventCreate:
    """
    Attributes:
        event_key (str):
        allowed_channels (list[EventCreateAllowedChannelsItem]):
        schema (EventCreateSchema):
        recipient_policy (EventCreateRecipientPolicy | Unset):
        compatibility (EventCreateCompatibility | Unset):  Default: EventCreateCompatibility.BACKWARD.
    """

    event_key: str
    allowed_channels: list[EventCreateAllowedChannelsItem]
    schema: EventCreateSchema
    recipient_policy: EventCreateRecipientPolicy | Unset = UNSET
    compatibility: EventCreateCompatibility | Unset = EventCreateCompatibility.BACKWARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_key = self.event_key

        allowed_channels = []
        for allowed_channels_item_data in self.allowed_channels:
            allowed_channels_item = allowed_channels_item_data.value
            allowed_channels.append(allowed_channels_item)

        schema = self.schema.to_dict()

        recipient_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient_policy, Unset):
            recipient_policy = self.recipient_policy.to_dict()

        compatibility: str | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_key": event_key,
                "allowed_channels": allowed_channels,
                "schema": schema,
            }
        )
        if recipient_policy is not UNSET:
            field_dict["recipient_policy"] = recipient_policy
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_create_recipient_policy import (
            EventCreateRecipientPolicy,  # noqa: PLC0415
        )
        from ..models.event_create_schema import EventCreateSchema  # noqa: PLC0415

        d = dict(src_dict)
        event_key = d.pop("event_key")

        allowed_channels = []
        _allowed_channels = d.pop("allowed_channels")
        for allowed_channels_item_data in _allowed_channels:
            allowed_channels_item = EventCreateAllowedChannelsItem(allowed_channels_item_data)

            allowed_channels.append(allowed_channels_item)

        schema = EventCreateSchema.from_dict(d.pop("schema"))

        _recipient_policy = d.pop("recipient_policy", UNSET)
        recipient_policy: EventCreateRecipientPolicy | Unset
        if isinstance(_recipient_policy, Unset):
            recipient_policy = UNSET
        else:
            recipient_policy = EventCreateRecipientPolicy.from_dict(_recipient_policy)

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: EventCreateCompatibility | Unset
        if isinstance(_compatibility, Unset):
            compatibility = UNSET
        else:
            compatibility = EventCreateCompatibility(_compatibility)

        event_create = cls(
            event_key=event_key,
            allowed_channels=allowed_channels,
            schema=schema,
            recipient_policy=recipient_policy,
            compatibility=compatibility,
        )

        event_create.additional_properties = d
        return event_create

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
