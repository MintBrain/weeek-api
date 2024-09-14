from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmMoveDealBody")


@_attrs_define
class CrmMoveDealBody:
    """
    Attributes:
        status_id (Union[None, Unset, str]):
        previous_deal_id (Union[None, Unset, str]): If null, the deal will be placed at the top
    """

    status_id: Union[None, Unset, str] = UNSET
    previous_deal_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_id: Union[None, Unset, str]
        if isinstance(self.status_id, Unset):
            status_id = UNSET
        else:
            status_id = self.status_id

        previous_deal_id: Union[None, Unset, str]
        if isinstance(self.previous_deal_id, Unset):
            previous_deal_id = UNSET
        else:
            previous_deal_id = self.previous_deal_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if previous_deal_id is not UNSET:
            field_dict["previousDealId"] = previous_deal_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_status_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status_id = _parse_status_id(d.pop("statusId", UNSET))

        def _parse_previous_deal_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous_deal_id = _parse_previous_deal_id(d.pop("previousDealId", UNSET))

        crm_move_deal_body = cls(
            status_id=status_id,
            previous_deal_id=previous_deal_id,
        )

        crm_move_deal_body.additional_properties = d
        return crm_move_deal_body

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
