from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmUpdateDealFunnelBody")


@_attrs_define
class CrmUpdateDealFunnelBody:
    """
    Attributes:
        funnel_id (Union[Unset, str]):
    """

    funnel_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        funnel_id = self.funnel_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if funnel_id is not UNSET:
            field_dict["funnelId"] = funnel_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        funnel_id = d.pop("funnelId", UNSET)

        crm_update_deal_funnel_body = cls(
            funnel_id=funnel_id,
        )

        crm_update_deal_funnel_body.additional_properties = d
        return crm_update_deal_funnel_body

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
