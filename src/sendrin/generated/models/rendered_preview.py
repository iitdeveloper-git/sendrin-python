from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rendered_preview_rendered import RenderedPreviewRendered


T = TypeVar("T", bound="RenderedPreview")


@_attrs_define
class RenderedPreview:
    """
    Attributes:
        rendered (RenderedPreviewRendered):
        locale (str):
        variant (str):
        version (int):
    """

    rendered: RenderedPreviewRendered
    locale: str
    variant: str
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rendered = self.rendered.to_dict()

        locale = self.locale

        variant = self.variant

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rendered": rendered,
                "locale": locale,
                "variant": variant,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rendered_preview_rendered import RenderedPreviewRendered  # noqa: PLC0415

        d = dict(src_dict)
        rendered = RenderedPreviewRendered.from_dict(d.pop("rendered"))

        locale = d.pop("locale")

        variant = d.pop("variant")

        version = d.pop("version")

        rendered_preview = cls(
            rendered=rendered,
            locale=locale,
            variant=variant,
            version=version,
        )

        rendered_preview.additional_properties = d
        return rendered_preview

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
