import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_address import OrganizationAddress
    from ..models.organization_email import OrganizationEmail
    from ..models.organization_phone import OrganizationPhone


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        id (Union[Unset, str]):
        creator_id (Union[Unset, str]):
        name (Union[Unset, str]):
        responsible_id (Union[None, Unset, str]):
        addresses (Union[Unset, List['OrganizationAddress']]):
        emails (Union[Unset, List['OrganizationEmail']]):
        phones (Union[Unset, List['OrganizationPhone']]):
        contacts (Union[Unset, List[str]]):
        tags (Union[Unset, List[int]]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    responsible_id: Union[None, Unset, str] = UNSET
    addresses: Union[Unset, List["OrganizationAddress"]] = UNSET
    emails: Union[Unset, List["OrganizationEmail"]] = UNSET
    phones: Union[Unset, List["OrganizationPhone"]] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    tags: Union[Unset, List[int]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        name = self.name

        responsible_id: Union[None, Unset, str]
        if isinstance(self.responsible_id, Unset):
            responsible_id = UNSET
        else:
            responsible_id = self.responsible_id

        addresses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

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

        contacts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts

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
        if name is not UNSET:
            field_dict["name"] = name
        if responsible_id is not UNSET:
            field_dict["responsibleId"] = responsible_id
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if tags is not UNSET:
            field_dict["tags"] = tags
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.organization_address import OrganizationAddress
        from ..models.organization_email import OrganizationEmail
        from ..models.organization_phone import OrganizationPhone

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_responsible_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        responsible_id = _parse_responsible_id(d.pop("responsibleId", UNSET))

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = OrganizationAddress.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = OrganizationEmail.from_dict(emails_item_data)

            emails.append(emails_item)

        phones = []
        _phones = d.pop("phones", UNSET)
        for phones_item_data in _phones or []:
            phones_item = OrganizationPhone.from_dict(phones_item_data)

            phones.append(phones_item)

        contacts = cast(List[str], d.pop("contacts", UNSET))

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

        organization = cls(
            id=id,
            creator_id=creator_id,
            name=name,
            responsible_id=responsible_id,
            addresses=addresses,
            emails=emails,
            phones=phones,
            contacts=contacts,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
        )

        organization.additional_properties = d
        return organization

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
