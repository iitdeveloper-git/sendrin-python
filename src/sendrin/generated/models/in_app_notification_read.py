from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_app_notification_read_action_payload import InAppNotificationReadActionPayload
    from ..models.in_app_notification_read_metadata_json import InAppNotificationReadMetadataJson
    from ..models.in_app_notification_read_toast_payload import InAppNotificationReadToastPayload


T = TypeVar("T", bound="InAppNotificationRead")


@_attrs_define
class InAppNotificationRead:
    """
    Attributes:
        id (str):
        event_key (str):
        title (str):
        message (str):
        severity (str):
        priority (int):
        action_payload (InAppNotificationReadActionPayload):
        toast_payload (InAppNotificationReadToastPayload):
        metadata_json (InAppNotificationReadMetadataJson):
        expires_at (datetime.datetime | None):
        created_at (datetime.datetime):
        read (bool | Unset):  Default: False.
        recipient_id (None | str | Unset):
        read_at (datetime.datetime | None | Unset):
        dismissed_at (datetime.datetime | None | Unset):
        opened_at (datetime.datetime | None | Unset):
    """

    id: str
    event_key: str
    title: str
    message: str
    severity: str
    priority: int
    action_payload: InAppNotificationReadActionPayload
    toast_payload: InAppNotificationReadToastPayload
    metadata_json: InAppNotificationReadMetadataJson
    expires_at: datetime.datetime | None
    created_at: datetime.datetime
    read: bool | Unset = False
    recipient_id: None | str | Unset = UNSET
    read_at: datetime.datetime | None | Unset = UNSET
    dismissed_at: datetime.datetime | None | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_key = self.event_key

        title = self.title

        message = self.message

        severity = self.severity

        priority = self.priority

        action_payload = self.action_payload.to_dict()

        toast_payload = self.toast_payload.to_dict()

        metadata_json = self.metadata_json.to_dict()

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        created_at = self.created_at.isoformat()

        read = self.read

        recipient_id: None | str | Unset
        if isinstance(self.recipient_id, Unset):
            recipient_id = UNSET
        else:
            recipient_id = self.recipient_id

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        elif isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at

        dismissed_at: None | str | Unset
        if isinstance(self.dismissed_at, Unset):
            dismissed_at = UNSET
        elif isinstance(self.dismissed_at, datetime.datetime):
            dismissed_at = self.dismissed_at.isoformat()
        else:
            dismissed_at = self.dismissed_at

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_key": event_key,
                "title": title,
                "message": message,
                "severity": severity,
                "priority": priority,
                "action_payload": action_payload,
                "toast_payload": toast_payload,
                "metadata_json": metadata_json,
                "expires_at": expires_at,
                "created_at": created_at,
            }
        )
        if read is not UNSET:
            field_dict["read"] = read
        if recipient_id is not UNSET:
            field_dict["recipient_id"] = recipient_id
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if dismissed_at is not UNSET:
            field_dict["dismissed_at"] = dismissed_at
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_app_notification_read_action_payload import (
            InAppNotificationReadActionPayload,  # noqa: PLC0415
        )
        from ..models.in_app_notification_read_metadata_json import (
            InAppNotificationReadMetadataJson,  # noqa: PLC0415
        )
        from ..models.in_app_notification_read_toast_payload import (
            InAppNotificationReadToastPayload,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        event_key = d.pop("event_key")

        title = d.pop("title")

        message = d.pop("message")

        severity = d.pop("severity")

        priority = d.pop("priority")

        action_payload = InAppNotificationReadActionPayload.from_dict(d.pop("action_payload"))

        toast_payload = InAppNotificationReadToastPayload.from_dict(d.pop("toast_payload"))

        metadata_json = InAppNotificationReadMetadataJson.from_dict(d.pop("metadata_json"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        read = d.pop("read", UNSET)

        def _parse_recipient_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recipient_id = _parse_recipient_id(d.pop("recipient_id", UNSET))

        def _parse_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = datetime.datetime.fromisoformat(data)

                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))

        def _parse_dismissed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dismissed_at_type_0 = datetime.datetime.fromisoformat(data)

                return dismissed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dismissed_at = _parse_dismissed_at(d.pop("dismissed_at", UNSET))

        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("opened_at", UNSET))

        in_app_notification_read = cls(
            id=id,
            event_key=event_key,
            title=title,
            message=message,
            severity=severity,
            priority=priority,
            action_payload=action_payload,
            toast_payload=toast_payload,
            metadata_json=metadata_json,
            expires_at=expires_at,
            created_at=created_at,
            read=read,
            recipient_id=recipient_id,
            read_at=read_at,
            dismissed_at=dismissed_at,
            opened_at=opened_at,
        )

        in_app_notification_read.additional_properties = d
        return in_app_notification_read

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
