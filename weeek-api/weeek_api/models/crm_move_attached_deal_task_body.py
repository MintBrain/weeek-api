from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmMoveAttachedDealTaskBody")


@_attrs_define
class CrmMoveAttachedDealTaskBody:
    """
    Attributes:
        previous_task_id (Union[None, Unset, int]): If null, task will be placed at the top
    """

    previous_task_id: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        previous_task_id: Union[None, Unset, int]
        if isinstance(self.previous_task_id, Unset):
            previous_task_id = UNSET
        else:
            previous_task_id = self.previous_task_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous_task_id is not UNSET:
            field_dict["previousTaskId"] = previous_task_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_previous_task_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        previous_task_id = _parse_previous_task_id(d.pop("previousTaskId", UNSET))

        crm_move_attached_deal_task_body = cls(
            previous_task_id=previous_task_id,
        )

        crm_move_attached_deal_task_body.additional_properties = d
        return crm_move_attached_deal_task_body

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
