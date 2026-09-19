from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_update_fallback_policy_type_0 import ProviderUpdateFallbackPolicyType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_update_public_config_type_0 import ProviderUpdatePublicConfigType0


T = TypeVar("T", bound="ProviderUpdate")


@_attrs_define
class ProviderUpdate:
    """
    Attributes:
        name (None | str | Unset):
        public_config (None | ProviderUpdatePublicConfigType0 | Unset):
        is_default (bool | None | Unset):
        fallback_policy (None | ProviderUpdateFallbackPolicyType0 | Unset):
        fallback_provider_id (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    public_config: None | ProviderUpdatePublicConfigType0 | Unset = UNSET
    is_default: bool | None | Unset = UNSET
    fallback_policy: None | ProviderUpdateFallbackPolicyType0 | Unset = UNSET
    fallback_provider_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_update_public_config_type_0 import (
            ProviderUpdatePublicConfigType0,  # noqa: PLC0415
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        public_config: dict[str, Any] | None | Unset
        if isinstance(self.public_config, Unset):
            public_config = UNSET
        elif isinstance(self.public_config, ProviderUpdatePublicConfigType0):
            public_config = self.public_config.to_dict()
        else:
            public_config = self.public_config

        is_default: bool | None | Unset
        if isinstance(self.is_default, Unset):
            is_default = UNSET
        else:
            is_default = self.is_default

        fallback_policy: None | str | Unset
        if isinstance(self.fallback_policy, Unset):
            fallback_policy = UNSET
        elif isinstance(self.fallback_policy, ProviderUpdateFallbackPolicyType0):
            fallback_policy = self.fallback_policy.value
        else:
            fallback_policy = self.fallback_policy

        fallback_provider_id: None | str | Unset
        if isinstance(self.fallback_provider_id, Unset):
            fallback_provider_id = UNSET
        else:
            fallback_provider_id = self.fallback_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if public_config is not UNSET:
            field_dict["public_config"] = public_config
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if fallback_policy is not UNSET:
            field_dict["fallback_policy"] = fallback_policy
        if fallback_provider_id is not UNSET:
            field_dict["fallback_provider_id"] = fallback_provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_update_public_config_type_0 import (
            ProviderUpdatePublicConfigType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_public_config(data: object) -> None | ProviderUpdatePublicConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                public_config_type_0 = ProviderUpdatePublicConfigType0.from_dict(data)

                return public_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderUpdatePublicConfigType0 | Unset, data)

        public_config = _parse_public_config(d.pop("public_config", UNSET))

        def _parse_is_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_default = _parse_is_default(d.pop("is_default", UNSET))

        def _parse_fallback_policy(
            data: object,
        ) -> None | ProviderUpdateFallbackPolicyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fallback_policy_type_0 = ProviderUpdateFallbackPolicyType0(data)

                return fallback_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderUpdateFallbackPolicyType0 | Unset, data)

        fallback_policy = _parse_fallback_policy(d.pop("fallback_policy", UNSET))

        def _parse_fallback_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fallback_provider_id = _parse_fallback_provider_id(d.pop("fallback_provider_id", UNSET))

        provider_update = cls(
            name=name,
            public_config=public_config,
            is_default=is_default,
            fallback_policy=fallback_policy,
            fallback_provider_id=fallback_provider_id,
        )

        provider_update.additional_properties = d
        return provider_update

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
