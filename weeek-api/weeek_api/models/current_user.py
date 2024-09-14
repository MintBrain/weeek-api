from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentUser")


@_attrs_define
class CurrentUser:
    """
    Attributes:
        id (Union[Unset, str]):
        email (Union[Unset, str]):
        logo_link (Union[Unset, str]):
        last_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        about (Union[Unset, str]):
        position (Union[Unset, str]):
        language (Union[Unset, str]):
        birth_date (Union[Unset, str]):
        country (Union[Unset, str]):
        time_zone (Union[Unset, str]):
        phone_number (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    logo_link: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    about: Union[Unset, str] = UNSET
    position: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    birth_date: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        email = self.email

        logo_link = self.logo_link

        last_name = self.last_name

        first_name = self.first_name

        middle_name = self.middle_name

        about = self.about

        position = self.position

        language = self.language

        birth_date = self.birth_date

        country = self.country

        time_zone = self.time_zone

        phone_number = self.phone_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if logo_link is not UNSET:
            field_dict["logoLink"] = logo_link
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if about is not UNSET:
            field_dict["about"] = about
        if position is not UNSET:
            field_dict["position"] = position
        if language is not UNSET:
            field_dict["language"] = language
        if birth_date is not UNSET:
            field_dict["birthDate"] = birth_date
        if country is not UNSET:
            field_dict["country"] = country
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        logo_link = d.pop("logoLink", UNSET)

        last_name = d.pop("lastName", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        about = d.pop("about", UNSET)

        position = d.pop("position", UNSET)

        language = d.pop("language", UNSET)

        birth_date = d.pop("birthDate", UNSET)

        country = d.pop("country", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        current_user = cls(
            id=id,
            email=email,
            logo_link=logo_link,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            about=about,
            position=position,
            language=language,
            birth_date=birth_date,
            country=country,
            time_zone=time_zone,
            phone_number=phone_number,
        )

        current_user.additional_properties = d
        return current_user

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
