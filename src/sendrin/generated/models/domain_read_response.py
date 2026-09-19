from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_record_instruction import DnsRecordInstruction


T = TypeVar("T", bound="DomainReadResponse")


@_attrs_define
class DomainReadResponse:
    """
    Attributes:
        id (str):
        tenant_id (str):
        name (str):
        status (str):
        dkim_selector (str):
        dkim_status (str):
        spf_status (str):
        return_path_status (str):
        dmarc_status (str):
        return_path_domain (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_verified_at (datetime.datetime | None | Unset):
        verification_error (None | str | Unset):
        dns_records (list[DnsRecordInstruction] | Unset):
    """

    id: str
    tenant_id: str
    name: str
    status: str
    dkim_selector: str
    dkim_status: str
    spf_status: str
    return_path_status: str
    dmarc_status: str
    return_path_domain: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_verified_at: datetime.datetime | None | Unset = UNSET
    verification_error: None | str | Unset = UNSET
    dns_records: list[DnsRecordInstruction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        name = self.name

        status = self.status

        dkim_selector = self.dkim_selector

        dkim_status = self.dkim_status

        spf_status = self.spf_status

        return_path_status = self.return_path_status

        dmarc_status = self.dmarc_status

        return_path_domain = self.return_path_domain

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_verified_at: None | str | Unset
        if isinstance(self.last_verified_at, Unset):
            last_verified_at = UNSET
        elif isinstance(self.last_verified_at, datetime.datetime):
            last_verified_at = self.last_verified_at.isoformat()
        else:
            last_verified_at = self.last_verified_at

        verification_error: None | str | Unset
        if isinstance(self.verification_error, Unset):
            verification_error = UNSET
        else:
            verification_error = self.verification_error

        dns_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_records, Unset):
            dns_records = []
            for dns_records_item_data in self.dns_records:
                dns_records_item = dns_records_item_data.to_dict()
                dns_records.append(dns_records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tenant_id": tenant_id,
                "name": name,
                "status": status,
                "dkim_selector": dkim_selector,
                "dkim_status": dkim_status,
                "spf_status": spf_status,
                "return_path_status": return_path_status,
                "dmarc_status": dmarc_status,
                "return_path_domain": return_path_domain,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_verified_at is not UNSET:
            field_dict["last_verified_at"] = last_verified_at
        if verification_error is not UNSET:
            field_dict["verification_error"] = verification_error
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_record_instruction import DnsRecordInstruction  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenant_id")

        name = d.pop("name")

        status = d.pop("status")

        dkim_selector = d.pop("dkim_selector")

        dkim_status = d.pop("dkim_status")

        spf_status = d.pop("spf_status")

        return_path_status = d.pop("return_path_status")

        dmarc_status = d.pop("dmarc_status")

        return_path_domain = d.pop("return_path_domain")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_last_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_verified_at = _parse_last_verified_at(d.pop("last_verified_at", UNSET))

        def _parse_verification_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verification_error = _parse_verification_error(d.pop("verification_error", UNSET))

        _dns_records = d.pop("dns_records", UNSET)
        dns_records: list[DnsRecordInstruction] | Unset = UNSET
        if _dns_records is not UNSET:
            dns_records = []
            for dns_records_item_data in _dns_records:
                dns_records_item = DnsRecordInstruction.from_dict(dns_records_item_data)

                dns_records.append(dns_records_item)

        domain_read_response = cls(
            id=id,
            tenant_id=tenant_id,
            name=name,
            status=status,
            dkim_selector=dkim_selector,
            dkim_status=dkim_status,
            spf_status=spf_status,
            return_path_status=return_path_status,
            dmarc_status=dmarc_status,
            return_path_domain=return_path_domain,
            created_at=created_at,
            updated_at=updated_at,
            last_verified_at=last_verified_at,
            verification_error=verification_error,
            dns_records=dns_records,
        )

        domain_read_response.additional_properties = d
        return domain_read_response

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
