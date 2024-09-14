from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task import Task


T = TypeVar("T", bound="PutTmTasksIdResponse200")


@_attrs_define
class PutTmTasksIdResponse200:
    """
    Attributes:
        task (Task):
        success (Union[Unset, bool]):
    """

    task: "Task"
    success: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task = self.task.to_dict()

        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task": task,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task import Task

        d = src_dict.copy()
        task = Task.from_dict(d.pop("task"))

        success = d.pop("success", UNSET)

        put_tm_tasks_id_response_200 = cls(
            task=task,
            success=success,
        )

        put_tm_tasks_id_response_200.additional_properties = d
        return put_tm_tasks_id_response_200

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
