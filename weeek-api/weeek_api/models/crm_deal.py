from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deal import Deal


T = TypeVar("T", bound="CrmDeal")


@_attrs_define
class CrmDeal:
    """
    Attributes:
        success (Union[Unset, bool]):
        deal (Union[Unset, Deal]):
    """

    success: Union[Unset, bool] = UNSET
    deal: Union[Unset, "Deal"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        deal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deal, Unset):
            deal = self.deal.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if deal is not UNSET:
            field_dict["deal"] = deal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deal import Deal

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _deal = d.pop("deal", UNSET)
        deal: Union[Unset, Deal]
        if isinstance(_deal, Unset):
            deal = UNSET
        else:
            deal = Deal.from_dict(_deal)

        crm_deal = cls(
            success=success,
            deal=deal,
        )

        crm_deal.additional_properties = d
        return crm_deal

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
