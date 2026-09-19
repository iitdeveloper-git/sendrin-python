from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TemplateRead")


@_attrs_define
class TemplateRead:
    """
    Attributes:
        id (str):
        application_id (str):
        event_id (str):
        channel (str):
        locale (str):
        variant (str):
        status (str):
        published_version (int | None):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    application_id: str
    event_id: str
    channel: str
    locale: str
    variant: str
    status: str
    published_version: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        application_id = self.application_id

        event_id = self.event_id

        channel = self.channel

        locale = self.locale

        variant = self.variant

        status = self.status

        published_version: int | None
        published_version = self.published_version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "application_id": application_id,
                "event_id": event_id,
                "channel": channel,
                "locale": locale,
                "variant": variant,
                "status": status,
                "published_version": published_version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        application_id = d.pop("application_id")

        event_id = d.pop("event_id")

        channel = d.pop("channel")

        locale = d.pop("locale")

        variant = d.pop("variant")

        status = d.pop("status")

        def _parse_published_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        published_version = _parse_published_version(d.pop("published_version"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        template_read = cls(
            id=id,
            application_id=application_id,
            event_id=event_id,
            channel=channel,
            locale=locale,
            variant=variant,
            status=status,
            published_version=published_version,
            created_at=created_at,
            updated_at=updated_at,
        )

        template_read.additional_properties = d
        return template_read

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
