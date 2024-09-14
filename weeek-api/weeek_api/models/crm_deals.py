from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deal import Deal


T = TypeVar("T", bound="CrmDeals")


@_attrs_define
class CrmDeals:
    """
    Attributes:
        success (Union[Unset, bool]):
        deals (Union[Unset, List['Deal']]):
        has_more_deals (Union[Unset, bool]):
    """

    success: Union[Unset, bool] = UNSET
    deals: Union[Unset, List["Deal"]] = UNSET
    has_more_deals: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        deals: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deals, Unset):
            deals = []
            for deals_item_data in self.deals:
                deals_item = deals_item_data.to_dict()
                deals.append(deals_item)

        has_more_deals = self.has_more_deals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if deals is not UNSET:
            field_dict["deals"] = deals
        if has_more_deals is not UNSET:
            field_dict["hasMoreDeals"] = has_more_deals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.deal import Deal

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        deals = []
        _deals = d.pop("deals", UNSET)
        for deals_item_data in _deals or []:
            deals_item = Deal.from_dict(deals_item_data)

            deals.append(deals_item)

        has_more_deals = d.pop("hasMoreDeals", UNSET)

        crm_deals = cls(
            success=success,
            deals=deals,
            has_more_deals=has_more_deals,
        )

        crm_deals.additional_properties = d
        return crm_deals

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
