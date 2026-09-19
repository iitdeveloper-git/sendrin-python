from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provider_connection_test_channel import ProviderConnectionTestChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_connection_test_public_config import ProviderConnectionTestPublicConfig
    from ..models.provider_connection_test_secret_config import ProviderConnectionTestSecretConfig


T = TypeVar("T", bound="ProviderConnectionTest")


@_attrs_define
class ProviderConnectionTest:
    """
    Attributes:
        provider_type (str):
        channel (ProviderConnectionTestChannel):
        public_config (ProviderConnectionTestPublicConfig | Unset):
        secret_config (ProviderConnectionTestSecretConfig | Unset):
        tenant_id (None | str | Unset):
        application_id (None | str | Unset):
    """

    provider_type: str
    channel: ProviderConnectionTestChannel
    public_config: ProviderConnectionTestPublicConfig | Unset = UNSET
    secret_config: ProviderConnectionTestSecretConfig | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    application_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider_type = self.provider_type

        channel = self.channel.value

        public_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.public_config, Unset):
            public_config = self.public_config.to_dict()

        secret_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secret_config, Unset):
            secret_config = self.secret_config.to_dict()

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        else:
            application_id = self.application_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider_type": provider_type,
                "channel": channel,
            }
        )
        if public_config is not UNSET:
            field_dict["public_config"] = public_config
        if secret_config is not UNSET:
            field_dict["secret_config"] = secret_config
        if tenant_id is not UNSET:
            field_dict["tenant_id"] = tenant_id
        if application_id is not UNSET:
            field_dict["application_id"] = application_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_connection_test_public_config import (
            ProviderConnectionTestPublicConfig,  # noqa: PLC0415
        )
        from ..models.provider_connection_test_secret_config import (
            ProviderConnectionTestSecretConfig,  # noqa: PLC0415
        )

        d = dict(src_dict)
        provider_type = d.pop("provider_type")

        channel = ProviderConnectionTestChannel(d.pop("channel"))

        _public_config = d.pop("public_config", UNSET)
        public_config: ProviderConnectionTestPublicConfig | Unset
        if isinstance(_public_config, Unset):
            public_config = UNSET
        else:
            public_config = ProviderConnectionTestPublicConfig.from_dict(_public_config)

        _secret_config = d.pop("secret_config", UNSET)
        secret_config: ProviderConnectionTestSecretConfig | Unset
        if isinstance(_secret_config, Unset):
            secret_config = UNSET
        else:
            secret_config = ProviderConnectionTestSecretConfig.from_dict(_secret_config)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenant_id", UNSET))

        def _parse_application_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_id = _parse_application_id(d.pop("application_id", UNSET))

        provider_connection_test = cls(
            provider_type=provider_type,
            channel=channel,
            public_config=public_config,
            secret_config=secret_config,
            tenant_id=tenant_id,
            application_id=application_id,
        )

        provider_connection_test.additional_properties = d
        return provider_connection_test

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
