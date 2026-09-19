from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.template_version_read_content import TemplateVersionReadContent
    from ..models.template_version_read_sample_data import TemplateVersionReadSampleData


T = TypeVar("T", bound="TemplateVersionRead")


@_attrs_define
class TemplateVersionRead:
    """
    Attributes:
        id (str):
        template_id (str):
        version (int):
        state (str):
        content (TemplateVersionReadContent):
        sample_data (TemplateVersionReadSampleData):
        validation_errors (list[str]):
        published_at (datetime.datetime | None):
        published_by (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: str
    template_id: str
    version: int
    state: str
    content: TemplateVersionReadContent
    sample_data: TemplateVersionReadSampleData
    validation_errors: list[str]
    published_at: datetime.datetime | None
    published_by: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        version = self.version

        state = self.state

        content = self.content.to_dict()

        sample_data = self.sample_data.to_dict()

        validation_errors = self.validation_errors

        published_at: None | str
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        published_by: None | str
        published_by = self.published_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "template_id": template_id,
                "version": version,
                "state": state,
                "content": content,
                "sample_data": sample_data,
                "validation_errors": validation_errors,
                "published_at": published_at,
                "published_by": published_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_version_read_content import (
            TemplateVersionReadContent,  # noqa: PLC0415
        )
        from ..models.template_version_read_sample_data import (
            TemplateVersionReadSampleData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        version = d.pop("version")

        state = d.pop("state")

        content = TemplateVersionReadContent.from_dict(d.pop("content"))

        sample_data = TemplateVersionReadSampleData.from_dict(d.pop("sample_data"))

        validation_errors = cast(list[str], d.pop("validation_errors"))

        def _parse_published_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        published_at = _parse_published_at(d.pop("published_at"))

        def _parse_published_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_by = _parse_published_by(d.pop("published_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        template_version_read = cls(
            id=id,
            template_id=template_id,
            version=version,
            state=state,
            content=content,
            sample_data=sample_data,
            validation_errors=validation_errors,
            published_at=published_at,
            published_by=published_by,
            created_at=created_at,
            updated_at=updated_at,
        )

        template_version_read.additional_properties = d
        return template_version_read

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
