import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_update_request_priority import TaskUpdateRequestPriority
from ..models.task_update_request_type import TaskUpdateRequestType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_update_request_custom_fields import TaskUpdateRequestCustomFields


T = TypeVar("T", bound="TaskUpdateRequest")


@_attrs_define
class TaskUpdateRequest:
    """
    Attributes:
        title (Union[None, Unset, str]):
        description (Union[None, Unset, str]): Html description of the task
        project_id (Union[None, Unset, int]):
        board_id (Union[None, Unset, int]):
        board_column_id (Union[None, Unset, int]):
        priority (Union[Unset, TaskUpdateRequestPriority]):
        type (Union[Unset, TaskUpdateRequestType]):
        start_date (Union[None, Unset, datetime.date]): The start date of the task in Y-m-d format.
            Cannot be provided with startDateTime or dueDateTime
        due_date (Union[None, Unset, datetime.date]): The due date of the task in Y-m-d format. Cannot be provided with
            startDateTime or dueDateTime
        start_date_time (Union[None, Unset, datetime.datetime]): The start datetime of the task in ISO 8601 format.
            Cannot be provided with startDate or dueDate
        due_date_time (Union[None, Unset, datetime.datetime]): The due datetime of the task in ISO 8601 format. Cannot
            be provided with startDate or dueDate
        tags (Union[Unset, List[int]]): Array of tag ids
        custom_fields (Union[Unset, TaskUpdateRequestCustomFields]): Key-value object with custom field id and custom
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

    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    project_id: Union[None, Unset, int] = UNSET
    board_id: Union[None, Unset, int] = UNSET
    board_column_id: Union[None, Unset, int] = UNSET
    priority: Union[Unset, TaskUpdateRequestPriority] = UNSET
    type: Union[Unset, TaskUpdateRequestType] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    due_date: Union[None, Unset, datetime.date] = UNSET
    start_date_time: Union[None, Unset, datetime.datetime] = UNSET
    due_date_time: Union[None, Unset, datetime.datetime] = UNSET
    tags: Union[Unset, List[int]] = UNSET
    custom_fields: Union[Unset, "TaskUpdateRequestCustomFields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

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

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        start_date_time: Union[None, Unset, str]
        if isinstance(self.start_date_time, Unset):
            start_date_time = UNSET
        elif isinstance(self.start_date_time, datetime.datetime):
            start_date_time = self.start_date_time.isoformat()
        else:
            start_date_time = self.start_date_time

        due_date_time: Union[None, Unset, str]
        if isinstance(self.due_date_time, Unset):
            due_date_time = UNSET
        elif isinstance(self.due_date_time, datetime.datetime):
            due_date_time = self.due_date_time.isoformat()
        else:
            due_date_time = self.due_date_time

        tags: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

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
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if board_column_id is not UNSET:
            field_dict["boardColumnId"] = board_column_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if type is not UNSET:
            field_dict["type"] = type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if due_date_time is not UNSET:
            field_dict["dueDateTime"] = due_date_time
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_update_request_custom_fields import TaskUpdateRequestCustomFields

        d = src_dict.copy()

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

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

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskUpdateRequestPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskUpdateRequestPriority(_priority)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TaskUpdateRequestType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TaskUpdateRequestType(_type)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data).date()

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))

        def _parse_start_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_time_type_0 = isoparse(data)

                return start_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date_time = _parse_start_date_time(d.pop("startDateTime", UNSET))

        def _parse_due_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_time_type_0 = isoparse(data)

                return due_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_date_time = _parse_due_date_time(d.pop("dueDateTime", UNSET))

        tags = cast(List[int], d.pop("tags", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, TaskUpdateRequestCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = TaskUpdateRequestCustomFields.from_dict(_custom_fields)

        task_update_request = cls(
            title=title,
            description=description,
            project_id=project_id,
            board_id=board_id,
            board_column_id=board_column_id,
            priority=priority,
            type=type,
            start_date=start_date,
            due_date=due_date,
            start_date_time=start_date_time,
            due_date_time=due_date_time,
            tags=tags,
            custom_fields=custom_fields,
        )

        task_update_request.additional_properties = d
        return task_update_request

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
