from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantCreditsResponse")


@_attrs_define
class TenantCreditsResponse:
    """
    Attributes:
        tenant_id (str): Tenant identifier
        credits_balance (int): Current available credit balance
        plan (str | Unset): Active plan tier Default: 'free_developer'.
    """

    tenant_id: str
    credits_balance: int
    plan: str | Unset = "free_developer"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        credits_balance = self.credits_balance

        plan = self.plan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant_id": tenant_id,
                "credits_balance": credits_balance,
            }
        )
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenant_id")

        credits_balance = d.pop("credits_balance")

        plan = d.pop("plan", UNSET)

        tenant_credits_response = cls(
            tenant_id=tenant_id,
            credits_balance=credits_balance,
            plan=plan,
        )

        tenant_credits_response.additional_properties = d
        return tenant_credits_response

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
