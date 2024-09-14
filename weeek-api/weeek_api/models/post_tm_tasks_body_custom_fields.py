from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTmTasksBodyCustomFields")


@_attrs_define
class PostTmTasksBodyCustomFields:
    """Key-value object with custom field id and custom field value for the task

    For example

    ```
    "customFields" : {
        "<text_custom_field_id>": "Text value",
        "<boolean_custom_field_id>": true,
        "<datetime_custom_field_id>": "<ISO 8601 datetime string>",
        "<select_custom_field_id>": "<custom_field_option_id>"
        "<multiselect_custom_field_id>": ["<custom_field_option_id>"],
        "<member_custom_field_id>": ["<user_id>"],
        "<contact_custom_field_id>": "<contact_id>",
        "<link_custom_field_id>": "Link value",
        "<approval_custom_field_id>": ["<user_id>"]
    }
    ```

    """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        post_tm_tasks_body_custom_fields = cls()

        post_tm_tasks_body_custom_fields.additional_properties = d
        return post_tm_tasks_body_custom_fields

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
