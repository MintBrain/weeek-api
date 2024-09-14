from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_tm_tasks_body_priority import PostTmTasksBodyPriority
from ..models.post_tm_tasks_body_type import PostTmTasksBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_tm_tasks_body_custom_fields import PostTmTasksBodyCustomFields


T = TypeVar("T", bound="PostTmTasksBody")


@_attrs_define
class PostTmTasksBody:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[None, Unset, str]):
        day (Union[None, Unset, str]):
        project_id (Union[None, Unset, int]):
        parent_id (Union[None, Unset, int]):
        user_id (Union[None, Unset, str]):
        type (Union[Unset, PostTmTasksBodyType]):
        priority (Union[Unset, PostTmTasksBodyPriority]):
        board_id (Union[None, Unset, int]):
        board_column_id (Union[None, Unset, int]):
        custom_fields (Union[Unset, PostTmTasksBodyCustomFields]): Key-value object with custom field id and custom
            field value for the task

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

    title: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    day: Union[None, Unset, str] = UNSET
    project_id: Union[None, Unset, int] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    type: Union[Unset, PostTmTasksBodyType] = UNSET
    priority: Union[Unset, PostTmTasksBodyPriority] = UNSET
    board_id: Union[None, Unset, int] = UNSET
    board_column_id: Union[None, Unset, int] = UNSET
    custom_fields: Union[Unset, "PostTmTasksBodyCustomFields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        day: Union[None, Unset, str]
        if isinstance(self.day, Unset):
            day = UNSET
        else:
            day = self.day

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        board_id: Union[None, Unset, int]
        if isinstance(self.board_id, Unset):
            board_id = UNSET
        else:
            board_id = self.board_id

        board_column_id: Union[None, Unset, int]
        if isinstance(self.board_column_id, Unset):
            board_column_id = UNSET
        else:
            board_column_id = self.board_column_id

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if day is not UNSET:
            field_dict["day"] = day
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if type is not UNSET:
            field_dict["type"] = type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if board_column_id is not UNSET:
            field_dict["boardColumnId"] = board_column_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_tm_tasks_body_custom_fields import PostTmTasksBodyCustomFields

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_day(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        day = _parse_day(d.pop("day", UNSET))

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, PostTmTasksBodyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PostTmTasksBodyType(_type)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, PostTmTasksBodyPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = PostTmTasksBodyPriority(_priority)

        def _parse_board_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        board_id = _parse_board_id(d.pop("boardId", UNSET))

        def _parse_board_column_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        board_column_id = _parse_board_column_id(d.pop("boardColumnId", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, PostTmTasksBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = PostTmTasksBodyCustomFields.from_dict(_custom_fields)

        post_tm_tasks_body = cls(
            title=title,
            description=description,
            day=day,
            project_id=project_id,
            parent_id=parent_id,
            user_id=user_id,
            type=type,
            priority=priority,
            board_id=board_id,
            board_column_id=board_column_id,
            custom_fields=custom_fields,
        )

        post_tm_tasks_body.additional_properties = d
        return post_tm_tasks_body

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
