from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PutTmProjectsIdBody")


@_attrs_define
class PutTmProjectsIdBody:
    """
    Attributes:
        name (str):
        logo (Union[None, str]):
        is_private (bool):
        description (Union[None, str]):
        color (str):
    """

    name: str
    logo: Union[None, str]
    is_private: bool
    description: Union[None, str]
    color: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        logo: Union[None, str]
        logo = self.logo

        is_private = self.is_private

        description: Union[None, str]
        description = self.description

        color = self.color

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "logo": logo,
                "isPrivate": is_private,
                "description": description,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_logo(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo = _parse_logo(d.pop("logo"))

        is_private = d.pop("isPrivate")

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        color = d.pop("color")

        put_tm_projects_id_body = cls(
            name=name,
            logo=logo,
            is_private=is_private,
            description=description,
            color=color,
        )

        put_tm_projects_id_body.additional_properties = d
        return put_tm_projects_id_body

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
