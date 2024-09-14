import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_type import TaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.custom_field_value import CustomFieldValue
    from ..models.task_workloads_item import TaskWorkloadsItem
    from ..models.time_entry import TimeEntry


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """
    Attributes:
        overdue (int):
        created_at (datetime.datetime): Date the task was created in ISO 8601 format
        updated_at (datetime.datetime): Date the task was last updated in ISO 8601 format
        time_entries (List['TimeEntry']):
        id (Union[Unset, int]):
        parent_id (Union[None, Unset, int]):
        title (Union[Unset, str]):
        description (Union[None, Unset, str]):
        duration (Union[None, Unset, int]): In minutes
        type (Union[Unset, TaskType]):
        priority (Union[None, Unset, int]): 0 - Low
            1 - Medium
            2 - High
            3 - Hold
        is_completed (Union[Unset, bool]):
        author_id (Union[Unset, str]): ID of the user who created the task
        user_id (Union[None, Unset, str]): ID of the user who is executing the task
        board_id (Union[None, Unset, int]):
        board_column_id (Union[None, Unset, int]):
        project_id (Union[None, Unset, int]):
        image (Union[None, Unset, str]):
        is_private (Union[Unset, bool]):
        start_date (Union[None, Unset, datetime.date]): Start date of the task in `Y-m-d` format
        start_date_time (Union[None, Unset, datetime.datetime]): Start date of the task in ISO 8601 format
        due_date (Union[None, Unset, datetime.date]): Due date of the task in `Y-m-d` format
        due_date_time (Union[None, Unset, datetime.datetime]): Due date of the task in ISO 8601 format
        tags (Union[Unset, List[int]]):
        subscribers (Union[Unset, List[str]]):
        sub_tasks (Union[Unset, List[int]]):
        workloads (Union[Unset, List['TaskWorkloadsItem']]):
        custom_fields (Union[Unset, List['CustomFieldValue']]):
        attachments (Union[Unset, List['Attachment']]):
    """

    overdue: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    time_entries: List["TimeEntry"]
    id: Union[Unset, int] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    duration: Union[None, Unset, int] = UNSET
    type: Union[Unset, TaskType] = UNSET
    priority: Union[None, Unset, int] = UNSET
    is_completed: Union[Unset, bool] = UNSET
    author_id: Union[Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    board_id: Union[None, Unset, int] = UNSET
    board_column_id: Union[None, Unset, int] = UNSET
    project_id: Union[None, Unset, int] = UNSET
    image: Union[None, Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    start_date_time: Union[None, Unset, datetime.datetime] = UNSET
    due_date: Union[None, Unset, datetime.date] = UNSET
    due_date_time: Union[None, Unset, datetime.datetime] = UNSET
    tags: Union[Unset, List[int]] = UNSET
    subscribers: Union[Unset, List[str]] = UNSET
    sub_tasks: Union[Unset, List[int]] = UNSET
    workloads: Union[Unset, List["TaskWorkloadsItem"]] = UNSET
    custom_fields: Union[Unset, List["CustomFieldValue"]] = UNSET
    attachments: Union[Unset, List["Attachment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        overdue = self.overdue

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        time_entries = []
        for time_entries_item_data in self.time_entries:
            time_entries_item = time_entries_item_data.to_dict()
            time_entries.append(time_entries_item)

        id = self.id

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        title = self.title

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        duration: Union[None, Unset, int]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        priority: Union[None, Unset, int]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        is_completed = self.is_completed

        author_id = self.author_id

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

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

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        image: Union[None, Unset, str]
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        is_private = self.is_private

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        start_date_time: Union[None, Unset, str]
        if isinstance(self.start_date_time, Unset):
            start_date_time = UNSET
        elif isinstance(self.start_date_time, datetime.datetime):
            start_date_time = self.start_date_time.isoformat()
        else:
            start_date_time = self.start_date_time

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

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

        subscribers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscribers, Unset):
            subscribers = self.subscribers

        sub_tasks: Union[Unset, List[int]] = UNSET
        if not isinstance(self.sub_tasks, Unset):
            sub_tasks = self.sub_tasks

        workloads: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workloads, Unset):
            workloads = []
            for workloads_item_data in self.workloads:
                workloads_item = workloads_item_data.to_dict()
                workloads.append(workloads_item)

        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "overdue": overdue,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "timeEntries": time_entries,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if duration is not UNSET:
            field_dict["duration"] = duration
        if type is not UNSET:
            field_dict["type"] = type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if is_completed is not UNSET:
            field_dict["isCompleted"] = is_completed
        if author_id is not UNSET:
            field_dict["authorId"] = author_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if board_column_id is not UNSET:
            field_dict["boardColumnId"] = board_column_id
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if image is not UNSET:
            field_dict["image"] = image
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if start_date_time is not UNSET:
            field_dict["startDateTime"] = start_date_time
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if due_date_time is not UNSET:
            field_dict["dueDateTime"] = due_date_time
        if tags is not UNSET:
            field_dict["tags"] = tags
        if subscribers is not UNSET:
            field_dict["subscribers"] = subscribers
        if sub_tasks is not UNSET:
            field_dict["subTasks"] = sub_tasks
        if workloads is not UNSET:
            field_dict["workloads"] = workloads
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment
        from ..models.custom_field_value import CustomFieldValue
        from ..models.task_workloads_item import TaskWorkloadsItem
        from ..models.time_entry import TimeEntry

        d = src_dict.copy()
        overdue = d.pop("overdue")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        time_entries = []
        _time_entries = d.pop("timeEntries")
        for time_entries_item_data in _time_entries:
            time_entries_item = TimeEntry.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        id = d.pop("id", UNSET)

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        title = d.pop("title", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, TaskType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TaskType(_type)

        def _parse_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        is_completed = d.pop("isCompleted", UNSET)

        author_id = d.pop("authorId", UNSET)

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

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

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("projectId", UNSET))

        def _parse_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image = _parse_image(d.pop("image", UNSET))

        is_private = d.pop("isPrivate", UNSET)

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

        subscribers = cast(List[str], d.pop("subscribers", UNSET))

        sub_tasks = cast(List[int], d.pop("subTasks", UNSET))

        workloads = []
        _workloads = d.pop("workloads", UNSET)
        for workloads_item_data in _workloads or []:
            workloads_item = TaskWorkloadsItem.from_dict(workloads_item_data)

            workloads.append(workloads_item)

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomFieldValue.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = Attachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        task = cls(
            overdue=overdue,
            created_at=created_at,
            updated_at=updated_at,
            time_entries=time_entries,
            id=id,
            parent_id=parent_id,
            title=title,
            description=description,
            duration=duration,
            type=type,
            priority=priority,
            is_completed=is_completed,
            author_id=author_id,
            user_id=user_id,
            board_id=board_id,
            board_column_id=board_column_id,
            project_id=project_id,
            image=image,
            is_private=is_private,
            start_date=start_date,
            start_date_time=start_date_time,
            due_date=due_date,
            due_date_time=due_date_time,
            tags=tags,
            subscribers=subscribers,
            sub_tasks=sub_tasks,
            workloads=workloads,
            custom_fields=custom_fields,
            attachments=attachments,
        )

        task.additional_properties = d
        return task

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
