from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_create_body_type import CustomFieldCreateBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_create_body_config_type_0 import CustomFieldCreateBodyConfigType0


T = TypeVar("T", bound="CustomFieldCreateBody")


@_attrs_define
class CustomFieldCreateBody:
    """
    Attributes:
        type (CustomFieldCreateBodyType):
        name (Union[None, Unset, str]):
        config (Union['CustomFieldCreateBodyConfigType0', None, Unset]):
    """

    type: CustomFieldCreateBodyType
    name: Union[None, Unset, str] = UNSET
    config: Union["CustomFieldCreateBodyConfigType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_field_create_body_config_type_0 import CustomFieldCreateBodyConfigType0

        type = self.type.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config: Union[Dict[str, Any], None, Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CustomFieldCreateBodyConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_create_body_config_type_0 import CustomFieldCreateBodyConfigType0

        d = src_dict.copy()
        type = CustomFieldCreateBodyType(d.pop("type"))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_config(data: object) -> Union["CustomFieldCreateBodyConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CustomFieldCreateBodyConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CustomFieldCreateBodyConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        custom_field_create_body = cls(
            type=type,
            name=name,
            config=config,
        )

        custom_field_create_body.additional_properties = d
        return custom_field_create_body

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
