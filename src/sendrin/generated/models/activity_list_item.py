from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_list_item_product import ActivityListItemProduct
from ..models.activity_list_item_status import ActivityListItemStatus

T = TypeVar("T", bound="ActivityListItem")


@_attrs_define
class ActivityListItem:
    """
    Attributes:
        id (str):
        product (ActivityListItemProduct):
        created_at (datetime.datetime):
        channel (str):
        recipient_masked (str):
        application_id (None | str):
        application_name (None | str):
        status (ActivityListItemStatus):
        provider (None | str):
        latency_ms (int | None):
    """

    id: str
    product: ActivityListItemProduct
    created_at: datetime.datetime
    channel: str
    recipient_masked: str
    application_id: None | str
    application_name: None | str
    status: ActivityListItemStatus
    provider: None | str
    latency_ms: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product = self.product.value

        created_at = self.created_at.isoformat()

        channel = self.channel

        recipient_masked = self.recipient_masked

        application_id: None | str
        application_id = self.application_id

        application_name: None | str
        application_name = self.application_name

        status = self.status.value

        provider: None | str
        provider = self.provider

        latency_ms: int | None
        latency_ms = self.latency_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product": product,
                "created_at": created_at,
                "channel": channel,
                "recipient_masked": recipient_masked,
                "application_id": application_id,
                "application_name": application_name,
                "status": status,
                "provider": provider,
                "latency_ms": latency_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        product = ActivityListItemProduct(d.pop("product"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        channel = d.pop("channel")

        recipient_masked = d.pop("recipient_masked")

        def _parse_application_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        application_id = _parse_application_id(d.pop("application_id"))

        def _parse_application_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        application_name = _parse_application_name(d.pop("application_name"))

        status = ActivityListItemStatus(d.pop("status"))

        def _parse_provider(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider = _parse_provider(d.pop("provider"))

        def _parse_latency_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))

        activity_list_item = cls(
            id=id,
            product=product,
            created_at=created_at,
            channel=channel,
            recipient_masked=recipient_masked,
            application_id=application_id,
            application_name=application_name,
            status=status,
            provider=provider,
            latency_ms=latency_ms,
        )

        activity_list_item.additional_properties = d
        return activity_list_item

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
