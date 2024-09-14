from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmOrganization1")


@_attrs_define
class CrmOrganization1:
    """
    Attributes:
        name (Union[Unset, str]):
        addresses (Union[Unset, List[str]]):
        emails (Union[Unset, List[str]]):
        phones (Union[Unset, List[str]]):
        responsibles (Union[Unset, List[str]]):
    """

    name: Union[Unset, str] = UNSET
    addresses: Union[Unset, List[str]] = UNSET
    emails: Union[Unset, List[str]] = UNSET
    phones: Union[Unset, List[str]] = UNSET
    responsibles: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = self.addresses

        emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones

        responsibles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.responsibles, Unset):
            responsibles = self.responsibles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if responsibles is not UNSET:
            field_dict["responsibles"] = responsibles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        addresses = cast(List[str], d.pop("addresses", UNSET))

        emails = cast(List[str], d.pop("emails", UNSET))

        phones = cast(List[str], d.pop("phones", UNSET))

        responsibles = cast(List[str], d.pop("responsibles", UNSET))

        crm_organization_1 = cls(
            name=name,
            addresses=addresses,
            emails=emails,
            phones=phones,
            responsibles=responsibles,
        )

        crm_organization_1.additional_properties = d
        return crm_organization_1

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
