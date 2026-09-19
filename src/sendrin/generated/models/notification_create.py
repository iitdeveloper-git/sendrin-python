from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_create_channel import NotificationCreateChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_create_data import NotificationCreateData
    from ..models.notification_create_metadata import NotificationCreateMetadata
    from ..models.notification_create_recipient import NotificationCreateRecipient


T = TypeVar("T", bound="NotificationCreate")


@_attrs_define
class NotificationCreate:
    """
    Attributes:
        event_key (str):
        channel (NotificationCreateChannel):
        recipient (NotificationCreateRecipient):
        data (NotificationCreateData):
        app_id (None | str | Unset):
        locale (None | str | Unset):
        variant (None | str | Unset):
        priority (int | Unset):  Default: 5.
        scheduled_at (datetime.datetime | None | Unset):
        metadata (NotificationCreateMetadata | Unset):
        expires_at (datetime.datetime | None | Unset):
    """

    event_key: str
    channel: NotificationCreateChannel
    recipient: NotificationCreateRecipient
    data: NotificationCreateData
    app_id: None | str | Unset = UNSET
    locale: None | str | Unset = UNSET
    variant: None | str | Unset = UNSET
    priority: int | Unset = 5
    scheduled_at: datetime.datetime | None | Unset = UNSET
    metadata: NotificationCreateMetadata | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_key = self.event_key

        channel = self.channel.value

        recipient = self.recipient.to_dict()

        data = self.data.to_dict()

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        variant: None | str | Unset
        if isinstance(self.variant, Unset):
            variant = UNSET
        else:
            variant = self.variant

        priority = self.priority

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_key": event_key,
                "channel": channel,
                "recipient": recipient,
                "data": data,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if variant is not UNSET:
            field_dict["variant"] = variant
        if priority is not UNSET:
            field_dict["priority"] = priority
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_create_data import NotificationCreateData  # noqa: PLC0415
        from ..models.notification_create_metadata import (
            NotificationCreateMetadata,  # noqa: PLC0415
        )
        from ..models.notification_create_recipient import (
            NotificationCreateRecipient,  # noqa: PLC0415
        )

        d = dict(src_dict)
        event_key = d.pop("event_key")

        channel = NotificationCreateChannel(d.pop("channel"))

        recipient = NotificationCreateRecipient.from_dict(d.pop("recipient"))

        data = NotificationCreateData.from_dict(d.pop("data"))

        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        def _parse_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant = _parse_variant(d.pop("variant", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: NotificationCreateMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = NotificationCreateMetadata.from_dict(_metadata)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        notification_create = cls(
            event_key=event_key,
            channel=channel,
            recipient=recipient,
            data=data,
            app_id=app_id,
            locale=locale,
            variant=variant,
            priority=priority,
            scheduled_at=scheduled_at,
            metadata=metadata,
            expires_at=expires_at,
        )

        notification_create.additional_properties = d
        return notification_create

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
