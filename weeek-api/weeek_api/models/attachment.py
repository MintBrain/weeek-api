import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attachment_service_enum import AttachmentServiceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """
    Attributes:
        id (str):
        creator_id (str):
        service (AttachmentServiceEnum):
        name (str):
        url (str): Attachment URL. If `service` is `weeek`, this URL will be available for an hour.
        created_at (datetime.datetime):
        size (Union[Unset, int]): The size of the attachment in bytes. Only present when `service` is `weeek`
    """

    id: str
    creator_id: str
    service: AttachmentServiceEnum
    name: str
    url: str
    created_at: datetime.datetime
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        service = self.service.value

        name = self.name

        url = self.url

        created_at = self.created_at.isoformat()

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "creatorId": creator_id,
                "service": service,
                "name": name,
                "url": url,
                "createdAt": created_at,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        creator_id = d.pop("creatorId")

        service = AttachmentServiceEnum(d.pop("service"))

        name = d.pop("name")

        url = d.pop("url")

        created_at = isoparse(d.pop("createdAt"))

        size = d.pop("size", UNSET)

        attachment = cls(
            id=id,
            creator_id=creator_id,
            service=service,
            name=name,
            url=url,
            created_at=created_at,
            size=size,
        )

        attachment.additional_properties = d
        return attachment

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
