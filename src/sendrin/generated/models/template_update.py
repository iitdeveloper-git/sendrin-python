from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_update_content_type_0 import TemplateUpdateContentType0
    from ..models.template_update_sample_data_type_0 import TemplateUpdateSampleDataType0


T = TypeVar("T", bound="TemplateUpdate")


@_attrs_define
class TemplateUpdate:
    """
    Attributes:
        content (None | TemplateUpdateContentType0 | Unset):
        sample_data (None | TemplateUpdateSampleDataType0 | Unset):
    """

    content: None | TemplateUpdateContentType0 | Unset = UNSET
    sample_data: None | TemplateUpdateSampleDataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_update_content_type_0 import (
            TemplateUpdateContentType0,  # noqa: PLC0415
        )
        from ..models.template_update_sample_data_type_0 import (
            TemplateUpdateSampleDataType0,  # noqa: PLC0415
        )

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, TemplateUpdateContentType0):
            content = self.content.to_dict()
        else:
            content = self.content

        sample_data: dict[str, Any] | None | Unset
        if isinstance(self.sample_data, Unset):
            sample_data = UNSET
        elif isinstance(self.sample_data, TemplateUpdateSampleDataType0):
            sample_data = self.sample_data.to_dict()
        else:
            sample_data = self.sample_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if sample_data is not UNSET:
            field_dict["sample_data"] = sample_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_update_content_type_0 import (
            TemplateUpdateContentType0,  # noqa: PLC0415
        )
        from ..models.template_update_sample_data_type_0 import (
            TemplateUpdateSampleDataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_content(data: object) -> None | TemplateUpdateContentType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = TemplateUpdateContentType0.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateUpdateContentType0 | Unset, data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_sample_data(data: object) -> None | TemplateUpdateSampleDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sample_data_type_0 = TemplateUpdateSampleDataType0.from_dict(data)

                return sample_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateUpdateSampleDataType0 | Unset, data)

        sample_data = _parse_sample_data(d.pop("sample_data", UNSET))

        template_update = cls(
            content=content,
            sample_data=sample_data,
        )

        template_update.additional_properties = d
        return template_update

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
