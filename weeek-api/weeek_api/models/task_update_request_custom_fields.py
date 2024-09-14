from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TaskUpdateRequestCustomFields")


@_attrs_define
class TaskUpdateRequestCustomFields:
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

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        task_update_request_custom_fields = cls()

        return task_update_request_custom_fields
