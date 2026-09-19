from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_create_channel import TemplateCreateChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_create_content import TemplateCreateContent
    from ..models.template_create_sample_data import TemplateCreateSampleData


T = TypeVar("T", bound="TemplateCreate")


@_attrs_define
class TemplateCreate:
    """
    Attributes:
        channel (TemplateCreateChannel):
        content (TemplateCreateContent):
        locale (str | Unset):  Default: 'en'.
        variant (str | Unset):  Default: 'default'.
        sample_data (TemplateCreateSampleData | Unset):
    """

    channel: TemplateCreateChannel
    content: TemplateCreateContent
    locale: str | Unset = "en"
    variant: str | Unset = "default"
    sample_data: TemplateCreateSampleData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        content = self.content.to_dict()

        locale = self.locale

        variant = self.variant

        sample_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_data, Unset):
            sample_data = self.sample_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "content": content,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale
        if variant is not UNSET:
            field_dict["variant"] = variant
        if sample_data is not UNSET:
            field_dict["sample_data"] = sample_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_create_content import TemplateCreateContent  # noqa: PLC0415
        from ..models.template_create_sample_data import TemplateCreateSampleData  # noqa: PLC0415

        d = dict(src_dict)
        channel = TemplateCreateChannel(d.pop("channel"))

        content = TemplateCreateContent.from_dict(d.pop("content"))

        locale = d.pop("locale", UNSET)

        variant = d.pop("variant", UNSET)

        _sample_data = d.pop("sample_data", UNSET)
        sample_data: TemplateCreateSampleData | Unset
        if isinstance(_sample_data, Unset):
            sample_data = UNSET
        else:
            sample_data = TemplateCreateSampleData.from_dict(_sample_data)

        template_create = cls(
            channel=channel,
            content=content,
            locale=locale,
            variant=variant,
            sample_data=sample_data,
        )

        template_create.additional_properties = d
        return template_create

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
