from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_detail_response_product import ActivityDetailResponseProduct
from ..models.activity_detail_response_status import ActivityDetailResponseStatus

if TYPE_CHECKING:
    from ..models.activity_detail_response_provider_response_type_0 import (
        ActivityDetailResponseProviderResponseType0,
    )
    from ..models.activity_detail_response_request_metadata import (
        ActivityDetailResponseRequestMetadata,
    )
    from ..models.activity_timeline_entry import ActivityTimelineEntry


T = TypeVar("T", bound="ActivityDetailResponse")


@_attrs_define
class ActivityDetailResponse:
    """
    Attributes:
        id (str):
        product (ActivityDetailResponseProduct):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (ActivityDetailResponseStatus):
        application_id (None | str):
        application_name (None | str):
        event_name (None | str):
        recipient_masked (str):
        channel (str):
        provider (None | str):
        provider_message_id (None | str):
        attempt_count (int):
        latency_ms (int | None):
        idempotency_key (None | str):
        timeline (list[ActivityTimelineEntry]):
        request_metadata (ActivityDetailResponseRequestMetadata):
        provider_response (ActivityDetailResponseProviderResponseType0 | None):
        failure_code (None | str):
        failure_reason (None | str):
        retry_allowed (bool):
    """

    id: str
    product: ActivityDetailResponseProduct
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: ActivityDetailResponseStatus
    application_id: None | str
    application_name: None | str
    event_name: None | str
    recipient_masked: str
    channel: str
    provider: None | str
    provider_message_id: None | str
    attempt_count: int
    latency_ms: int | None
    idempotency_key: None | str
    timeline: list[ActivityTimelineEntry]
    request_metadata: ActivityDetailResponseRequestMetadata
    provider_response: ActivityDetailResponseProviderResponseType0 | None
    failure_code: None | str
    failure_reason: None | str
    retry_allowed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_detail_response_provider_response_type_0 import (
            ActivityDetailResponseProviderResponseType0,  # noqa: PLC0415
        )

        id = self.id

        product = self.product.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status = self.status.value

        application_id: None | str
        application_id = self.application_id

        application_name: None | str
        application_name = self.application_name

        event_name: None | str
        event_name = self.event_name

        recipient_masked = self.recipient_masked

        channel = self.channel

        provider: None | str
        provider = self.provider

        provider_message_id: None | str
        provider_message_id = self.provider_message_id

        attempt_count = self.attempt_count

        latency_ms: int | None
        latency_ms = self.latency_ms

        idempotency_key: None | str
        idempotency_key = self.idempotency_key

        timeline = []
        for timeline_item_data in self.timeline:
            timeline_item = timeline_item_data.to_dict()
            timeline.append(timeline_item)

        request_metadata = self.request_metadata.to_dict()

        provider_response: dict[str, Any] | None
        if isinstance(self.provider_response, ActivityDetailResponseProviderResponseType0):
            provider_response = self.provider_response.to_dict()
        else:
            provider_response = self.provider_response

        failure_code: None | str
        failure_code = self.failure_code

        failure_reason: None | str
        failure_reason = self.failure_reason

        retry_allowed = self.retry_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "product": product,
                "created_at": created_at,
                "updated_at": updated_at,
                "status": status,
                "application_id": application_id,
                "application_name": application_name,
                "event_name": event_name,
                "recipient_masked": recipient_masked,
                "channel": channel,
                "provider": provider,
                "provider_message_id": provider_message_id,
                "attempt_count": attempt_count,
                "latency_ms": latency_ms,
                "idempotency_key": idempotency_key,
                "timeline": timeline,
                "request_metadata": request_metadata,
                "provider_response": provider_response,
                "failure_code": failure_code,
                "failure_reason": failure_reason,
                "retry_allowed": retry_allowed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_detail_response_provider_response_type_0 import (
            ActivityDetailResponseProviderResponseType0,  # noqa: PLC0415
        )
        from ..models.activity_detail_response_request_metadata import (
            ActivityDetailResponseRequestMetadata,  # noqa: PLC0415
        )
        from ..models.activity_timeline_entry import ActivityTimelineEntry  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        product = ActivityDetailResponseProduct(d.pop("product"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status = ActivityDetailResponseStatus(d.pop("status"))

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

        def _parse_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_name = _parse_event_name(d.pop("event_name"))

        recipient_masked = d.pop("recipient_masked")

        channel = d.pop("channel")

        def _parse_provider(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider = _parse_provider(d.pop("provider"))

        def _parse_provider_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_message_id = _parse_provider_message_id(d.pop("provider_message_id"))

        attempt_count = d.pop("attempt_count")

        def _parse_latency_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))

        def _parse_idempotency_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        idempotency_key = _parse_idempotency_key(d.pop("idempotency_key"))

        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in _timeline:
            timeline_item = ActivityTimelineEntry.from_dict(timeline_item_data)

            timeline.append(timeline_item)

        request_metadata = ActivityDetailResponseRequestMetadata.from_dict(
            d.pop("request_metadata")
        )

        def _parse_provider_response(
            data: object,
        ) -> ActivityDetailResponseProviderResponseType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_response_type_0 = ActivityDetailResponseProviderResponseType0.from_dict(
                    data
                )

                return provider_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActivityDetailResponseProviderResponseType0 | None, data)

        provider_response = _parse_provider_response(d.pop("provider_response"))

        def _parse_failure_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure_code = _parse_failure_code(d.pop("failure_code"))

        def _parse_failure_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason"))

        retry_allowed = d.pop("retry_allowed")

        activity_detail_response = cls(
            id=id,
            product=product,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            application_id=application_id,
            application_name=application_name,
            event_name=event_name,
            recipient_masked=recipient_masked,
            channel=channel,
            provider=provider,
            provider_message_id=provider_message_id,
            attempt_count=attempt_count,
            latency_ms=latency_ms,
            idempotency_key=idempotency_key,
            timeline=timeline,
            request_metadata=request_metadata,
            provider_response=provider_response,
            failure_code=failure_code,
            failure_reason=failure_reason,
            retry_allowed=retry_allowed,
        )

        activity_detail_response.additional_properties = d
        return activity_detail_response

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
