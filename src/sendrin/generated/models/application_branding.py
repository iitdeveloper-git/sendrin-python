from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationBranding")


@_attrs_define
class ApplicationBranding:
    """
    Attributes:
        display_name (None | str | Unset):
        logo_url (None | str | Unset):
        brand_color (str | Unset):  Default: '#16a34a'.
        sender_name (None | str | Unset):
        sender_handle (str | Unset):  Default: 'auth'.
        support_email (None | str | Unset):
        website_url (None | str | Unset):
        reply_to (None | str | Unset):
    """

    display_name: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    brand_color: str | Unset = "#16a34a"
    sender_name: None | str | Unset = UNSET
    sender_handle: str | Unset = "auth"
    support_email: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    reply_to: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        brand_color = self.brand_color

        sender_name: None | str | Unset
        if isinstance(self.sender_name, Unset):
            sender_name = UNSET
        else:
            sender_name = self.sender_name

        sender_handle = self.sender_handle

        support_email: None | str | Unset
        if isinstance(self.support_email, Unset):
            support_email = UNSET
        else:
            support_email = self.support_email

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        reply_to: None | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if brand_color is not UNSET:
            field_dict["brand_color"] = brand_color
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name
        if sender_handle is not UNSET:
            field_dict["sender_handle"] = sender_handle
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        brand_color = d.pop("brand_color", UNSET)

        def _parse_sender_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_name = _parse_sender_name(d.pop("sender_name", UNSET))

        sender_handle = d.pop("sender_handle", UNSET)

        def _parse_support_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        support_email = _parse_support_email(d.pop("support_email", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_reply_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        application_branding = cls(
            display_name=display_name,
            logo_url=logo_url,
            brand_color=brand_color,
            sender_name=sender_name,
            sender_handle=sender_handle,
            support_email=support_email,
            website_url=website_url,
            reply_to=reply_to,
        )

        application_branding.additional_properties = d
        return application_branding

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
