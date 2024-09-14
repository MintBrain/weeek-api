import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_email import ContactEmail
    from ..models.contact_phone import ContactPhone


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        id (Union[Unset, str]):
        creator_id (Union[Unset, str]):
        last_name (Union[None, Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[None, Unset, str]):
        organizations (Union[Unset, List[str]]):
        emails (Union[Unset, List['ContactEmail']]):
        phones (Union[Unset, List['ContactPhone']]):
        tags (Union[Unset, List[int]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[None, Unset, str] = UNSET
    organizations: Union[Unset, List[str]] = UNSET
    emails: Union[Unset, List["ContactEmail"]] = UNSET
    phones: Union[Unset, List["ContactPhone"]] = UNSET
    tags: Union[Unset, List[int]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        first_name = self.first_name

        middle_name: Union[None, Unset, str]
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        organizations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organizations, Unset):
            organizations = self.organizations

        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        phones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        tags: Union[Unset, List[int]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact_email import ContactEmail
        from ..models.contact_phone import ContactPhone

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        first_name = d.pop("firstName", UNSET)

        def _parse_middle_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))

        organizations = cast(List[str], d.pop("organizations", UNSET))

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = ContactEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in _phones or []:
            phones_item = ContactPhone.from_dict(phones_item_data)

            phones.append(phones_item)

        tags = cast(List[int], d.pop("tags", UNSET))

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

        contact = cls(
            id=id,
            creator_id=creator_id,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            organizations=organizations,
            emails=emails,
            phones=phones,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
        )

        contact.additional_properties = d
        return contact

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
