from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (Union[Unset, str]):
        email (Union[Unset, str]):
        logo (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        first_name (Union[None, Unset, str]):
        middle_name (Union[None, Unset, str]):
        position (Union[None, Unset, str]):
        time_zone (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    logo: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    middle_name: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        email = self.email

        logo: Union[None, Unset, str]
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        middle_name: Union[None, Unset, str]
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        time_zone = self.time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if logo is not UNSET:
            field_dict["logo"] = logo
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if position is not UNSET:
            field_dict["position"] = position
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        def _parse_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_middle_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        middle_name = _parse_middle_name(d.pop("middleName", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        position = _parse_position(d.pop("position", UNSET))

        time_zone = d.pop("timeZone", UNSET)

        user = cls(
            id=id,
            email=email,
            logo=logo,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            position=position,
            time_zone=time_zone,
        )

        user.additional_properties = d
        return user

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
