from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_create_channel import ProviderCreateChannel
from ..models.provider_create_fallback_policy import ProviderCreateFallbackPolicy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_create_public_config import ProviderCreatePublicConfig
    from ..models.provider_create_secret_config_type_0 import ProviderCreateSecretConfigType0


T = TypeVar("T", bound="ProviderCreate")


@_attrs_define
class ProviderCreate:
    """
    Attributes:
        channel (ProviderCreateChannel):
        provider_type (str):
        name (str):
        public_config (ProviderCreatePublicConfig | Unset):
        secret_config (None | ProviderCreateSecretConfigType0 | Unset):
        is_default (bool | Unset):  Default: False.
        fallback_policy (ProviderCreateFallbackPolicy | Unset):  Default: ProviderCreateFallbackPolicy.NONE.
        fallback_provider_id (None | str | Unset):
    """

    channel: ProviderCreateChannel
    provider_type: str
    name: str
    public_config: ProviderCreatePublicConfig | Unset = UNSET
    secret_config: None | ProviderCreateSecretConfigType0 | Unset = UNSET
    is_default: bool | Unset = False
    fallback_policy: ProviderCreateFallbackPolicy | Unset = ProviderCreateFallbackPolicy.NONE
    fallback_provider_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_create_secret_config_type_0 import (
            ProviderCreateSecretConfigType0,  # noqa: PLC0415
        )

        channel = self.channel.value

        provider_type = self.provider_type

        name = self.name

        public_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_config, Unset):
            public_config = self.public_config.to_dict()

        secret_config: dict[str, Any] | None | Unset
        if isinstance(self.secret_config, Unset):
            secret_config = UNSET
        elif isinstance(self.secret_config, ProviderCreateSecretConfigType0):
            secret_config = self.secret_config.to_dict()
        else:
            secret_config = self.secret_config

        is_default = self.is_default

        fallback_policy: str | Unset = UNSET
        if not isinstance(self.fallback_policy, Unset):
            fallback_policy = self.fallback_policy.value

        fallback_provider_id: None | str | Unset
        if isinstance(self.fallback_provider_id, Unset):
            fallback_provider_id = UNSET
        else:
            fallback_provider_id = self.fallback_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "provider_type": provider_type,
                "name": name,
            }
        )
        if public_config is not UNSET:
            field_dict["public_config"] = public_config
        if secret_config is not UNSET:
            field_dict["secret_config"] = secret_config
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if fallback_policy is not UNSET:
            field_dict["fallback_policy"] = fallback_policy
        if fallback_provider_id is not UNSET:
            field_dict["fallback_provider_id"] = fallback_provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_create_public_config import (
            ProviderCreatePublicConfig,  # noqa: PLC0415
        )
        from ..models.provider_create_secret_config_type_0 import (
            ProviderCreateSecretConfigType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        channel = ProviderCreateChannel(d.pop("channel"))

        provider_type = d.pop("provider_type")

        name = d.pop("name")

        _public_config = d.pop("public_config", UNSET)
        public_config: ProviderCreatePublicConfig | Unset
        if isinstance(_public_config, Unset):
            public_config = UNSET
        else:
            public_config = ProviderCreatePublicConfig.from_dict(_public_config)

        def _parse_secret_config(data: object) -> None | ProviderCreateSecretConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secret_config_type_0 = ProviderCreateSecretConfigType0.from_dict(data)

                return secret_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderCreateSecretConfigType0 | Unset, data)

        secret_config = _parse_secret_config(d.pop("secret_config", UNSET))

        is_default = d.pop("is_default", UNSET)

        _fallback_policy = d.pop("fallback_policy", UNSET)
        fallback_policy: ProviderCreateFallbackPolicy | Unset
        if isinstance(_fallback_policy, Unset):
            fallback_policy = UNSET
        else:
            fallback_policy = ProviderCreateFallbackPolicy(_fallback_policy)

        def _parse_fallback_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fallback_provider_id = _parse_fallback_provider_id(d.pop("fallback_provider_id", UNSET))

        provider_create = cls(
            channel=channel,
            provider_type=provider_type,
            name=name,
            public_config=public_config,
            secret_config=secret_config,
            is_default=is_default,
            fallback_policy=fallback_policy,
            fallback_provider_id=fallback_provider_id,
        )

        provider_create.additional_properties = d
        return provider_create

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
