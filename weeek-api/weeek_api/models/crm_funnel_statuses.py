from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel_status import FunnelStatus


T = TypeVar("T", bound="CrmFunnelStatuses")


@_attrs_define
class CrmFunnelStatuses:
    """
    Attributes:
        success (Union[Unset, bool]):
        statuses (Union[Unset, List['FunnelStatus']]):
    """

    success: Union[Unset, bool] = UNSET
    statuses: Union[Unset, List["FunnelStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()
                statuses.append(statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if statuses is not UNSET:
            field_dict["statuses"] = statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.funnel_status import FunnelStatus

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = FunnelStatus.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        crm_funnel_statuses = cls(
            success=success,
            statuses=statuses,
        )

        crm_funnel_statuses.additional_properties = d
        return crm_funnel_statuses

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
