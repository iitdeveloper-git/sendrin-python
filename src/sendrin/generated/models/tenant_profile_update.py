from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantProfileUpdate")


@_attrs_define
class TenantProfileUpdate:
    """
    Attributes:
        name (str):
        app_name (None | str | Unset):
        website_url (None | str | Unset):
        logo_url (None | str | Unset):
        mobile_number (None | str | Unset):
        whatsapp_number (None | str | Unset):
    """

    name: str
    app_name: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    mobile_number: None | str | Unset = UNSET
    whatsapp_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        app_name: None | str | Unset
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        mobile_number: None | str | Unset
        if isinstance(self.mobile_number, Unset):
            mobile_number = UNSET
        else:
            mobile_number = self.mobile_number

        whatsapp_number: None | str | Unset
        if isinstance(self.whatsapp_number, Unset):
            whatsapp_number = UNSET
        else:
            whatsapp_number = self.whatsapp_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if mobile_number is not UNSET:
            field_dict["mobile_number"] = mobile_number
        if whatsapp_number is not UNSET:
            field_dict["whatsapp_number"] = whatsapp_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_app_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_name = _parse_app_name(d.pop("app_name", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_mobile_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mobile_number = _parse_mobile_number(d.pop("mobile_number", UNSET))

        def _parse_whatsapp_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        whatsapp_number = _parse_whatsapp_number(d.pop("whatsapp_number", UNSET))

        tenant_profile_update = cls(
            name=name,
            app_name=app_name,
            website_url=website_url,
            logo_url=logo_url,
            mobile_number=mobile_number,
            whatsapp_number=whatsapp_number,
        )

        tenant_profile_update.additional_properties = d
        return tenant_profile_update

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
