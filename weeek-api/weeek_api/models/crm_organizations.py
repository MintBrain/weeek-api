from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization


T = TypeVar("T", bound="CrmOrganizations")


@_attrs_define
class CrmOrganizations:
    """
    Attributes:
        success (Union[Unset, bool]):
        organizations (Union[Unset, List['Organization']]):
    """

    success: Union[Unset, bool] = UNSET
    organizations: Union[Unset, List["Organization"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        organizations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = []
            for organizations_item_data in self.organizations:
                organizations_item = organizations_item_data.to_dict()
                organizations.append(organizations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if organizations is not UNSET:
            field_dict["organizations"] = organizations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization import Organization

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        organizations = []
        _organizations = d.pop("organizations", UNSET)
        for organizations_item_data in _organizations or []:
            organizations_item = Organization.from_dict(organizations_item_data)

            organizations.append(organizations_item)

        crm_organizations = cls(
            success=success,
            organizations=organizations,
        )

        crm_organizations.additional_properties = d
        return crm_organizations

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
