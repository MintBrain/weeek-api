from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task import Task


T = TypeVar("T", bound="CrmDealAttachTaskResponse200")


@_attrs_define
class CrmDealAttachTaskResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        task (Union[Unset, Task]):
    """

    success: Union[Unset, bool] = UNSET
    task: Union[Unset, "Task"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if task is not UNSET:
            field_dict["task"] = task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task import Task

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _task = d.pop("task", UNSET)
        task: Union[Unset, Task]
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = Task.from_dict(_task)

        crm_deal_attach_task_response_200 = cls(
            success=success,
            task=task,
        )

        crm_deal_attach_task_response_200.additional_properties = d
        return crm_deal_attach_task_response_200

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
