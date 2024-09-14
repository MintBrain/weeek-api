from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import Contact


T = TypeVar("T", bound="CrmContact")


@_attrs_define
class CrmContact:
    """
    Attributes:
        success (Union[Unset, bool]):
        contact (Union[Unset, Contact]):
    """

    success: Union[Unset, bool] = UNSET
    contact: Union[Unset, "Contact"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact import Contact

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, Contact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = Contact.from_dict(_contact)

        crm_contact = cls(
            success=success,
            contact=contact,
        )

        crm_contact.additional_properties = d
        return crm_contact

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
