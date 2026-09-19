from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_update_compatibility import EventUpdateCompatibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_update_recipient_policy_type_0 import EventUpdateRecipientPolicyType0
    from ..models.event_update_schema_type_0 import EventUpdateSchemaType0


T = TypeVar("T", bound="EventUpdate")


@_attrs_define
class EventUpdate:
    """
    Attributes:
        allowed_channels (list[str] | None | Unset):
        recipient_policy (EventUpdateRecipientPolicyType0 | None | Unset):
        schema (EventUpdateSchemaType0 | None | Unset):
        compatibility (EventUpdateCompatibility | Unset):  Default: EventUpdateCompatibility.BACKWARD.
    """

    allowed_channels: list[str] | None | Unset = UNSET
    recipient_policy: EventUpdateRecipientPolicyType0 | None | Unset = UNSET
    schema: EventUpdateSchemaType0 | None | Unset = UNSET
    compatibility: EventUpdateCompatibility | Unset = EventUpdateCompatibility.BACKWARD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_update_recipient_policy_type_0 import (
            EventUpdateRecipientPolicyType0,  # noqa: PLC0415
        )
        from ..models.event_update_schema_type_0 import EventUpdateSchemaType0  # noqa: PLC0415

        allowed_channels: list[str] | None | Unset
        if isinstance(self.allowed_channels, Unset):
            allowed_channels = UNSET
        elif isinstance(self.allowed_channels, list):
            allowed_channels = self.allowed_channels

        else:
            allowed_channels = self.allowed_channels

        recipient_policy: dict[str, Any] | None | Unset
        if isinstance(self.recipient_policy, Unset):
            recipient_policy = UNSET
        elif isinstance(self.recipient_policy, EventUpdateRecipientPolicyType0):
            recipient_policy = self.recipient_policy.to_dict()
        else:
            recipient_policy = self.recipient_policy

        schema: dict[str, Any] | None | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, EventUpdateSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        compatibility: str | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_channels is not UNSET:
            field_dict["allowed_channels"] = allowed_channels
        if recipient_policy is not UNSET:
            field_dict["recipient_policy"] = recipient_policy
        if schema is not UNSET:
            field_dict["schema"] = schema
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_update_recipient_policy_type_0 import (
            EventUpdateRecipientPolicyType0,  # noqa: PLC0415
        )
        from ..models.event_update_schema_type_0 import EventUpdateSchemaType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_allowed_channels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_channels_type_0 = cast(list[str], data)

                return allowed_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_channels = _parse_allowed_channels(d.pop("allowed_channels", UNSET))

        def _parse_recipient_policy(data: object) -> EventUpdateRecipientPolicyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                recipient_policy_type_0 = EventUpdateRecipientPolicyType0.from_dict(data)

                return recipient_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventUpdateRecipientPolicyType0 | None | Unset, data)

        recipient_policy = _parse_recipient_policy(d.pop("recipient_policy", UNSET))

        def _parse_schema(data: object) -> EventUpdateSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = EventUpdateSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventUpdateSchemaType0 | None | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: EventUpdateCompatibility | Unset
        if isinstance(_compatibility, Unset):
            compatibility = UNSET
        else:
            compatibility = EventUpdateCompatibility(_compatibility)

        event_update = cls(
            allowed_channels=allowed_channels,
            recipient_policy=recipient_policy,
            schema=schema,
            compatibility=compatibility,
        )

        event_update.additional_properties = d
        return event_update

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
