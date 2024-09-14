from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteCrmOrganizationsOrganizationIdContactsBody")


@_attrs_define
class DeleteCrmOrganizationsOrganizationIdContactsBody:
    """
    Attributes:
        contact_id (str):
    """

    contact_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_id = self.contact_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contactId": contact_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_id = d.pop("contactId")

        delete_crm_organizations_organization_id_contacts_body = cls(
            contact_id=contact_id,
        )

        delete_crm_organizations_organization_id_contacts_body.additional_properties = d
        return delete_crm_organizations_organization_id_contacts_body

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
