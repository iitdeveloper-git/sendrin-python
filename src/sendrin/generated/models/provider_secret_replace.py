from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.provider_secret_replace_secret_config import ProviderSecretReplaceSecretConfig


T = TypeVar("T", bound="ProviderSecretReplace")


@_attrs_define
class ProviderSecretReplace:
    """
    Attributes:
        secret_config (ProviderSecretReplaceSecretConfig):
    """

    secret_config: ProviderSecretReplaceSecretConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_config = self.secret_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret_config": secret_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_secret_replace_secret_config import (
            ProviderSecretReplaceSecretConfig,  # noqa: PLC0415
        )

        d = dict(src_dict)
        secret_config = ProviderSecretReplaceSecretConfig.from_dict(d.pop("secret_config"))

        provider_secret_replace = cls(
            secret_config=secret_config,
        )

        provider_secret_replace.additional_properties = d
        return provider_secret_replace

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
