from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task import Task


T = TypeVar("T", bound="GetTmTasksResponse200")


@_attrs_define
class GetTmTasksResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        tasks (Union[Unset, List['Task']]):
        has_more (Union[Unset, bool]):
    """

    success: Union[Unset, bool] = UNSET
    tasks: Union[Unset, List["Task"]] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

        has_more = self.has_more

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task import Task

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        has_more = d.pop("hasMore", UNSET)

        get_tm_tasks_response_200 = cls(
            success=success,
            tasks=tasks,
            has_more=has_more,
        )

        get_tm_tasks_response_200.additional_properties = d
        return get_tm_tasks_response_200

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
