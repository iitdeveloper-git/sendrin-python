from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_read_event_data import NotificationReadEventData
    from ..models.notification_read_metadata_json import NotificationReadMetadataJson
    from ..models.notification_read_recipient import NotificationReadRecipient


T = TypeVar("T", bound="NotificationRead")


@_attrs_define
class NotificationRead:
    """
    Attributes:
        id (str):
        application_id (str):
        event_key (str):
        channel (str):
        recipient (NotificationReadRecipient):
        event_data (NotificationReadEventData):
        metadata_json (NotificationReadMetadataJson):
        locale (None | str):
        variant (None | str):
        priority (int):
        correlation_id (None | str):
        status (str):
        scheduled_at (datetime.datetime | None):
        next_attempt_at (datetime.datetime | None):
        failure_code (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    application_id: str
    event_key: str
    channel: str
    recipient: NotificationReadRecipient
    event_data: NotificationReadEventData
    metadata_json: NotificationReadMetadataJson
    locale: None | str
    variant: None | str
    priority: int
    correlation_id: None | str
    status: str
    scheduled_at: datetime.datetime | None
    next_attempt_at: datetime.datetime | None
    failure_code: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        application_id = self.application_id

        event_key = self.event_key

        channel = self.channel

        recipient = self.recipient.to_dict()

        event_data = self.event_data.to_dict()

        metadata_json = self.metadata_json.to_dict()

        locale: None | str
        locale = self.locale

        variant: None | str
        variant = self.variant

        priority = self.priority

        correlation_id: None | str
        correlation_id = self.correlation_id

        status = self.status

        scheduled_at: None | str
        if isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        next_attempt_at: None | str
        if isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        failure_code: None | str
        failure_code = self.failure_code

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "application_id": application_id,
                "event_key": event_key,
                "channel": channel,
                "recipient": recipient,
                "event_data": event_data,
                "metadata_json": metadata_json,
                "locale": locale,
                "variant": variant,
                "priority": priority,
                "correlation_id": correlation_id,
                "status": status,
                "scheduled_at": scheduled_at,
                "next_attempt_at": next_attempt_at,
                "failure_code": failure_code,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_read_event_data import NotificationReadEventData  # noqa: PLC0415
        from ..models.notification_read_metadata_json import (
            NotificationReadMetadataJson,  # noqa: PLC0415
        )
        from ..models.notification_read_recipient import NotificationReadRecipient  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        application_id = d.pop("application_id")

        event_key = d.pop("event_key")

        channel = d.pop("channel")

        recipient = NotificationReadRecipient.from_dict(d.pop("recipient"))

        event_data = NotificationReadEventData.from_dict(d.pop("event_data"))

        metadata_json = NotificationReadMetadataJson.from_dict(d.pop("metadata_json"))

        def _parse_locale(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        locale = _parse_locale(d.pop("locale"))

        def _parse_variant(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        variant = _parse_variant(d.pop("variant"))

        priority = d.pop("priority")

        def _parse_correlation_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        correlation_id = _parse_correlation_id(d.pop("correlation_id"))

        status = d.pop("status")

        def _parse_scheduled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at"))

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at"))

        def _parse_failure_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure_code = _parse_failure_code(d.pop("failure_code"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        notification_read = cls(
            id=id,
            application_id=application_id,
            event_key=event_key,
            channel=channel,
            recipient=recipient,
            event_data=event_data,
            metadata_json=metadata_json,
            locale=locale,
            variant=variant,
            priority=priority,
            correlation_id=correlation_id,
            status=status,
            scheduled_at=scheduled_at,
            next_attempt_at=next_attempt_at,
            failure_code=failure_code,
            created_at=created_at,
            updated_at=updated_at,
        )

        notification_read.additional_properties = d
        return notification_read

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
