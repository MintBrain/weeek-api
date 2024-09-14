from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_email import ContactEmail


T = TypeVar("T", bound="EmailResponse1")


@_attrs_define
class EmailResponse1:
    """
    Attributes:
        email (ContactEmail):
        success (Union[Unset, bool]):  Default: True.
    """

    email: "ContactEmail"
    success: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email.to_dict()

        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_email import ContactEmail

        d = src_dict.copy()
        email = ContactEmail.from_dict(d.pop("email"))

        success = d.pop("success", UNSET)

        email_response_1 = cls(
            email=email,
            success=success,
        )

        email_response_1.additional_properties = d
        return email_response_1

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
