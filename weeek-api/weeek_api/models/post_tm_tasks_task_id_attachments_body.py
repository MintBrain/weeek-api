from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="PostTmTasksTaskIdAttachmentsBody")


@_attrs_define
class PostTmTasksTaskIdAttachmentsBody:
    """
    Attributes:
        files (File): Max file size is 100MB
    """

    files: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        files = self.files.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files[]": files,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        files = self.files.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "files[]": files,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        files = File(payload=BytesIO(d.pop("files[]")))

        post_tm_tasks_task_id_attachments_body = cls(
            files=files,
        )

        post_tm_tasks_task_id_attachments_body.additional_properties = d
        return post_tm_tasks_task_id_attachments_body

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
