from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_workloads_item_type import TaskWorkloadsItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskWorkloadsItem")


@_attrs_define
class TaskWorkloadsItem:
    """
    Attributes:
        id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        type (Union[Unset, TaskWorkloadsItemType]): 1 - auto calculated from timer
            2 - manual added
        date (Union[Unset, str]):
        duration (Union[Unset, int]):
        work_start_at (Union[None, Unset, str]):
        work_end_at (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    type: Union[Unset, TaskWorkloadsItemType] = UNSET
    date: Union[Unset, str] = UNSET
    duration: Union[Unset, int] = UNSET
    work_start_at: Union[None, Unset, str] = UNSET
    work_end_at: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        date = self.date

        duration = self.duration

        work_start_at: Union[None, Unset, str]
        if isinstance(self.work_start_at, Unset):
            work_start_at = UNSET
        else:
            work_start_at = self.work_start_at

        work_end_at: Union[None, Unset, str]
        if isinstance(self.work_end_at, Unset):
            work_end_at = UNSET
        else:
            work_end_at = self.work_end_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if type is not UNSET:
            field_dict["type"] = type
        if date is not UNSET:
            field_dict["date"] = date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if work_start_at is not UNSET:
            field_dict["workStartAt"] = work_start_at
        if work_end_at is not UNSET:
            field_dict["workEndAt"] = work_end_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("userId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TaskWorkloadsItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TaskWorkloadsItemType(_type)

        date = d.pop("date", UNSET)

        duration = d.pop("duration", UNSET)

        def _parse_work_start_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_start_at = _parse_work_start_at(d.pop("workStartAt", UNSET))

        def _parse_work_end_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        work_end_at = _parse_work_end_at(d.pop("workEndAt", UNSET))

        task_workloads_item = cls(
            id=id,
            user_id=user_id,
            type=type,
            date=date,
            duration=duration,
            work_start_at=work_start_at,
            work_end_at=work_end_at,
        )

        task_workloads_item.additional_properties = d
        return task_workloads_item

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
