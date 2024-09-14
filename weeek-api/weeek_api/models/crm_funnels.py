from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel import Funnel


T = TypeVar("T", bound="CrmFunnels")


@_attrs_define
class CrmFunnels:
    """
    Attributes:
        success (Union[Unset, bool]):
        funnels (Union[Unset, List['Funnel']]):
    """

    success: Union[Unset, bool] = UNSET
    funnels: Union[Unset, List["Funnel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        funnels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.funnels, Unset):
            funnels = []
            for funnels_item_data in self.funnels:
                funnels_item = funnels_item_data.to_dict()
                funnels.append(funnels_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if funnels is not UNSET:
            field_dict["funnels"] = funnels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.funnel import Funnel

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        funnels = []
        _funnels = d.pop("funnels", UNSET)
        for funnels_item_data in _funnels or []:
            funnels_item = Funnel.from_dict(funnels_item_data)

            funnels.append(funnels_item)

        crm_funnels = cls(
            success=success,
            funnels=funnels,
        )

        crm_funnels.additional_properties = d
        return crm_funnels

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
