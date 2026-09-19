from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_read_public_config import ProviderReadPublicConfig


T = TypeVar("T", bound="ProviderRead")


@_attrs_define
class ProviderRead:
    """
    Attributes:
        id (str):
        tenant_id (str):
        application_id (None | str):
        channel (str):
        provider_type (str):
        name (str):
        public_config (ProviderReadPublicConfig):
        active (bool):
        is_default (bool):
        fallback_policy (str):
        fallback_provider_id (None | str):
        health_status (str):
        verified_at (datetime.datetime | None):
        last_error_code (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        secret_configured (bool | Unset):  Default: False.
    """

    id: str
    tenant_id: str
    application_id: None | str
    channel: str
    provider_type: str
    name: str
    public_config: ProviderReadPublicConfig
    active: bool
    is_default: bool
    fallback_policy: str
    fallback_provider_id: None | str
    health_status: str
    verified_at: datetime.datetime | None
    last_error_code: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    secret_configured: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        application_id: None | str
        application_id = self.application_id

        channel = self.channel

        provider_type = self.provider_type

        name = self.name

        public_config = self.public_config.to_dict()

        active = self.active

        is_default = self.is_default

        fallback_policy = self.fallback_policy

        fallback_provider_id: None | str
        fallback_provider_id = self.fallback_provider_id

        health_status = self.health_status

        verified_at: None | str
        if isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        last_error_code: None | str
        last_error_code = self.last_error_code

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        secret_configured = self.secret_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tenant_id": tenant_id,
                "application_id": application_id,
                "channel": channel,
                "provider_type": provider_type,
                "name": name,
                "public_config": public_config,
                "active": active,
                "is_default": is_default,
                "fallback_policy": fallback_policy,
                "fallback_provider_id": fallback_provider_id,
                "health_status": health_status,
                "verified_at": verified_at,
                "last_error_code": last_error_code,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if secret_configured is not UNSET:
            field_dict["secret_configured"] = secret_configured

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_read_public_config import ProviderReadPublicConfig  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenant_id")

        def _parse_application_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        application_id = _parse_application_id(d.pop("application_id"))

        channel = d.pop("channel")

        provider_type = d.pop("provider_type")

        name = d.pop("name")

        public_config = ProviderReadPublicConfig.from_dict(d.pop("public_config"))

        active = d.pop("active")

        is_default = d.pop("is_default")

        fallback_policy = d.pop("fallback_policy")

        def _parse_fallback_provider_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fallback_provider_id = _parse_fallback_provider_id(d.pop("fallback_provider_id"))

        health_status = d.pop("health_status")

        def _parse_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        verified_at = _parse_verified_at(d.pop("verified_at"))

        def _parse_last_error_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error_code = _parse_last_error_code(d.pop("last_error_code"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        secret_configured = d.pop("secret_configured", UNSET)

        provider_read = cls(
            id=id,
            tenant_id=tenant_id,
            application_id=application_id,
            channel=channel,
            provider_type=provider_type,
            name=name,
            public_config=public_config,
            active=active,
            is_default=is_default,
            fallback_policy=fallback_policy,
            fallback_provider_id=fallback_provider_id,
            health_status=health_status,
            verified_at=verified_at,
            last_error_code=last_error_code,
            created_at=created_at,
            updated_at=updated_at,
            secret_configured=secret_configured,
        )

        provider_read.additional_properties = d
        return provider_read

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
