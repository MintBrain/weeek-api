from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_phone import OrganizationPhone


T = TypeVar("T", bound="PhoneResponse")


@_attrs_define
class PhoneResponse:
    """
    Attributes:
        phone (OrganizationPhone):
        success (Union[Unset, bool]):  Default: True.
    """

    phone: "OrganizationPhone"
    success: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone = self.phone.to_dict()

        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone": phone,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_phone import OrganizationPhone

        d = src_dict.copy()
        phone = OrganizationPhone.from_dict(d.pop("phone"))

        success = d.pop("success", UNSET)

        phone_response = cls(
            phone=phone,
            success=success,
        )

        phone_response.additional_properties = d
        return phone_response

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
