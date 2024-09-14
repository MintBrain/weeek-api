from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_option_color import CustomFieldOptionColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldOption")


@_attrs_define
class CustomFieldOption:
    """
    Attributes:
        name (str):
        color (CustomFieldOptionColor):
        id (Union[Unset, str]):
    """

    name: str
    color: CustomFieldOptionColor
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        color = self.color.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "color": color,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        color = CustomFieldOptionColor(d.pop("color"))

        id = d.pop("id", UNSET)

        custom_field_option = cls(
            name=name,
            color=color,
            id=id,
        )

        custom_field_option.additional_properties = d
        return custom_field_option

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
