from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        id (Union[Unset, int]):
        title (Union[Unset, str]):
        logo_link (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        color (Union[Unset, str]):
        is_private (Union[Unset, bool]):
        team (Union[Unset, List[str]]):
        custom_fields (Union[Unset, List['CustomField']]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    logo_link: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    team: Union[Unset, List[str]] = UNSET
    custom_fields: Union[Unset, List["CustomField"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        logo_link: Union[None, Unset, str]
        if isinstance(self.logo_link, Unset):
            logo_link = UNSET
        else:
            logo_link = self.logo_link

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        color = self.color

        is_private = self.is_private

        team: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team

        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if logo_link is not UNSET:
            field_dict["logoLink"] = logo_link
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if team is not UNSET:
            field_dict["team"] = team
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field import CustomField

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        def _parse_logo_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_link = _parse_logo_link(d.pop("logoLink", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        color = d.pop("color", UNSET)

        is_private = d.pop("isPrivate", UNSET)

        team = cast(List[str], d.pop("team", UNSET))

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        project = cls(
            id=id,
            title=title,
            logo_link=logo_link,
            description=description,
            color=color,
            is_private=is_private,
            team=team,
            custom_fields=custom_fields,
        )

        project.additional_properties = d
        return project

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
