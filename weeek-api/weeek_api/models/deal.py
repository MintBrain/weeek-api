import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.deal_win_status import DealWinStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment import Attachment
    from ..models.custom_field_value import CustomFieldValue
    from ..models.task import Task


T = TypeVar("T", bound="Deal")


@_attrs_define
class Deal:
    """
    Attributes:
        id (Union[Unset, str]): String identifier unique only within this resource in the workspace.
        creator_id (Union[Unset, str]):
        funnel_id (Union[Unset, str]):
        status_id (Union[Unset, str]):
        assignees (Union[Unset, List[str]]):
        organizations (Union[Unset, List[str]]):
        contacts (Union[Unset, List[str]]):
        title (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        amount (Union[None, Unset, float]):
        win_status (Union[Unset, DealWinStatus]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        tags (Union[Unset, List[int]]):
        tasks (Union[Unset, List['Task']]):
        custom_fields (Union[Unset, List['CustomFieldValue']]):
        attachments (Union[Unset, List['Attachment']]):
    """

    id: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    funnel_id: Union[Unset, str] = UNSET
    status_id: Union[Unset, str] = UNSET
    assignees: Union[Unset, List[str]] = UNSET
    organizations: Union[Unset, List[str]] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    title: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    amount: Union[None, Unset, float] = UNSET
    win_status: Union[Unset, DealWinStatus] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    tags: Union[Unset, List[int]] = UNSET
    tasks: Union[Unset, List["Task"]] = UNSET
    custom_fields: Union[Unset, List["CustomFieldValue"]] = UNSET
    attachments: Union[Unset, List["Attachment"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        funnel_id = self.funnel_id

        status_id = self.status_id

        assignees: Union[Unset, List[str]] = UNSET
        if not isinstance(self.assignees, Unset):
            assignees = self.assignees

        organizations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = self.organizations

        contacts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts

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

        amount: Union[None, Unset, float]
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        win_status: Union[Unset, str] = UNSET
        if not isinstance(self.win_status, Unset):
            win_status = self.win_status.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        tags: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()
                tasks.append(tasks_item)

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
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if funnel_id is not UNSET:
            field_dict["funnelId"] = funnel_id
        if status_id is not UNSET:
            field_dict["statusId"] = status_id
        if assignees is not UNSET:
            field_dict["assignees"] = assignees
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if win_status is not UNSET:
            field_dict["winStatus"] = win_status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment import Attachment
        from ..models.custom_field_value import CustomFieldValue
        from ..models.task import Task

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        funnel_id = d.pop("funnelId", UNSET)

        status_id = d.pop("statusId", UNSET)

        assignees = cast(List[str], d.pop("assignees", UNSET))

        organizations = cast(List[str], d.pop("organizations", UNSET))

        contacts = cast(List[str], d.pop("contacts", UNSET))

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

        def _parse_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        amount = _parse_amount(d.pop("amount", UNSET))

        _win_status = d.pop("winStatus", UNSET)
        win_status: Union[Unset, DealWinStatus]
        if isinstance(_win_status, Unset):
            win_status = UNSET
        else:
            win_status = DealWinStatus(_win_status)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        tags = cast(List[int], d.pop("tags", UNSET))

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

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

        deal = cls(
            id=id,
            creator_id=creator_id,
            funnel_id=funnel_id,
            status_id=status_id,
            assignees=assignees,
            organizations=organizations,
            contacts=contacts,
            title=title,
            description=description,
            amount=amount,
            win_status=win_status,
            created_at=created_at,
            updated_at=updated_at,
            tags=tags,
            tasks=tasks,
            custom_fields=custom_fields,
            attachments=attachments,
        )

        deal.additional_properties = d
        return deal

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
