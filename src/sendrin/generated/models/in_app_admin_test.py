from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_app_admin_test_data import InAppAdminTestData
    from ..models.in_app_admin_test_metadata import InAppAdminTestMetadata
    from ..models.in_app_admin_test_recipient import InAppAdminTestRecipient


T = TypeVar("T", bound="InAppAdminTest")


@_attrs_define
class InAppAdminTest:
    """
    Attributes:
        application_id (str):
        event_key (str):
        recipient (InAppAdminTestRecipient):
        data (InAppAdminTestData):
        priority (int | Unset):  Default: 5.
        metadata (InAppAdminTestMetadata | Unset):
    """

    application_id: str
    event_key: str
    recipient: InAppAdminTestRecipient
    data: InAppAdminTestData
    priority: int | Unset = 5
    metadata: InAppAdminTestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        event_key = self.event_key

        recipient = self.recipient.to_dict()

        data = self.data.to_dict()

        priority = self.priority

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "application_id": application_id,
                "event_key": event_key,
                "recipient": recipient,
                "data": data,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_app_admin_test_data import InAppAdminTestData  # noqa: PLC0415
        from ..models.in_app_admin_test_metadata import InAppAdminTestMetadata  # noqa: PLC0415
        from ..models.in_app_admin_test_recipient import InAppAdminTestRecipient  # noqa: PLC0415

        d = dict(src_dict)
        application_id = d.pop("application_id")

        event_key = d.pop("event_key")

        recipient = InAppAdminTestRecipient.from_dict(d.pop("recipient"))

        data = InAppAdminTestData.from_dict(d.pop("data"))

        priority = d.pop("priority", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: InAppAdminTestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InAppAdminTestMetadata.from_dict(_metadata)

        in_app_admin_test = cls(
            application_id=application_id,
            event_key=event_key,
            recipient=recipient,
            data=data,
            priority=priority,
            metadata=metadata,
        )

        in_app_admin_test.additional_properties = d
        return in_app_admin_test

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
