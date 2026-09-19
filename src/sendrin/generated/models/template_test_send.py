from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_test_send_data_type_0 import TemplateTestSendDataType0
    from ..models.template_test_send_recipient import TemplateTestSendRecipient


T = TypeVar("T", bound="TemplateTestSend")


@_attrs_define
class TemplateTestSend:
    """
    Attributes:
        recipient (TemplateTestSendRecipient):
        data (None | TemplateTestSendDataType0 | Unset):
    """

    recipient: TemplateTestSendRecipient
    data: None | TemplateTestSendDataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_test_send_data_type_0 import (
            TemplateTestSendDataType0,  # noqa: PLC0415
        )

        recipient = self.recipient.to_dict()

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, TemplateTestSendDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recipient": recipient,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_test_send_data_type_0 import (
            TemplateTestSendDataType0,  # noqa: PLC0415
        )
        from ..models.template_test_send_recipient import TemplateTestSendRecipient  # noqa: PLC0415

        d = dict(src_dict)
        recipient = TemplateTestSendRecipient.from_dict(d.pop("recipient"))

        def _parse_data(data: object) -> None | TemplateTestSendDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = TemplateTestSendDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateTestSendDataType0 | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        template_test_send = cls(
            recipient=recipient,
            data=data,
        )

        template_test_send.additional_properties = d
        return template_test_send

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
