from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CrmContact1")


@_attrs_define
class CrmContact1:
    """
    Attributes:
        first_name (str):
        last_name (Union[None, Unset, str]):
        middle_name (Union[None, Unset, str]):
        organizations (Union[List[str], None, Unset]):
        emails (Union[List[str], None, Unset]):
        phones (Union[List[str], None, Unset]):
        tags (Union[List[int], None, Unset]):
    """

    first_name: str
    last_name: Union[None, Unset, str] = UNSET
    middle_name: Union[None, Unset, str] = UNSET
    organizations: Union[List[str], None, Unset] = UNSET
    emails: Union[List[str], None, Unset] = UNSET
    phones: Union[List[str], None, Unset] = UNSET
    tags: Union[List[int], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        middle_name: Union[None, Unset, str]
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        organizations: Union[List[str], None, Unset]
        if isinstance(self.organizations, Unset):
            organizations = UNSET
        elif isinstance(self.organizations, list):
            organizations = self.organizations

        else:
            organizations = self.organizations

        emails: Union[List[str], None, Unset]
        if isinstance(self.emails, Unset):
            emails = UNSET
        elif isinstance(self.emails, list):
            emails = self.emails

        else:
            emails = self.emails

        phones: Union[List[str], None, Unset]
        if isinstance(self.phones, Unset):
            phones = UNSET
        elif isinstance(self.phones, list):
            phones = self.phones

        else:
            phones = self.phones

        tags: Union[List[int], None, Unset]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
            }
        )
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_middle_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))

        def _parse_organizations(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organizations_type_0 = cast(List[str], data)

                return organizations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        organizations = _parse_organizations(d.pop("organizations", UNSET))

        def _parse_emails(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                emails_type_0 = cast(List[str], data)

                return emails_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        emails = _parse_emails(d.pop("emails", UNSET))

        def _parse_phones(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phones_type_0 = cast(List[str], data)

                return phones_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        phones = _parse_phones(d.pop("phones", UNSET))

        def _parse_tags(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(List[int], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        crm_contact_1 = cls(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            organizations=organizations,
            emails=emails,
            phones=phones,
            tags=tags,
        )

        crm_contact_1.additional_properties = d
        return crm_contact_1

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
