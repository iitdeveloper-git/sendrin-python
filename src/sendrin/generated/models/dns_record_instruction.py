from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_record_instruction_purpose import DnsRecordInstructionPurpose
from ..models.dns_record_instruction_record_type import DnsRecordInstructionRecordType
from ..models.dns_record_instruction_status import DnsRecordInstructionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsRecordInstruction")


@_attrs_define
class DnsRecordInstruction:
    """
    Attributes:
        record_type (DnsRecordInstructionRecordType):
        name (str): Host / Name for DNS entry
        value (str): Target value for DNS entry
        purpose (DnsRecordInstructionPurpose):
        description (str):
        status (DnsRecordInstructionStatus | Unset):  Default: DnsRecordInstructionStatus.PENDING.
        ttl (int | Unset):  Default: 300.
    """

    record_type: DnsRecordInstructionRecordType
    name: str
    value: str
    purpose: DnsRecordInstructionPurpose
    description: str
    status: DnsRecordInstructionStatus | Unset = DnsRecordInstructionStatus.PENDING
    ttl: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_type = self.record_type.value

        name = self.name

        value = self.value

        purpose = self.purpose.value

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        ttl = self.ttl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_type": record_type,
                "name": name,
                "value": value,
                "purpose": purpose,
                "description": description,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_type = DnsRecordInstructionRecordType(d.pop("record_type"))

        name = d.pop("name")

        value = d.pop("value")

        purpose = DnsRecordInstructionPurpose(d.pop("purpose"))

        description = d.pop("description")

        _status = d.pop("status", UNSET)
        status: DnsRecordInstructionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DnsRecordInstructionStatus(_status)

        ttl = d.pop("ttl", UNSET)

        dns_record_instruction = cls(
            record_type=record_type,
            name=name,
            value=value,
            purpose=purpose,
            description=description,
            status=status,
            ttl=ttl,
        )

        dns_record_instruction.additional_properties = d
        return dns_record_instruction

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
