from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_type import CustomFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_config_type_0 import CustomFieldConfigType0
    from ..models.custom_field_option import CustomFieldOption


T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """
    Attributes:
        type (CustomFieldType):
        options (List['CustomFieldOption']): Only for select and multiselect custom fields
        id (Union[Unset, str]):
        name (Union[None, Unset, str]):
        config (Union['CustomFieldConfigType0', None, Unset]):
    """

    type: CustomFieldType
    options: List["CustomFieldOption"]
    id: Union[Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    config: Union["CustomFieldConfigType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_field_config_type_0 import CustomFieldConfigType0

        type = self.type.value

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config: Union[Dict[str, Any], None, Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CustomFieldConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "options": options,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_config_type_0 import CustomFieldConfigType0
        from ..models.custom_field_option import CustomFieldOption

        d = src_dict.copy()
        type = CustomFieldType(d.pop("type"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CustomFieldOption.from_dict(options_item_data)

            options.append(options_item)

        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_config(data: object) -> Union["CustomFieldConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CustomFieldConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CustomFieldConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        custom_field = cls(
            type=type,
            options=options,
            id=id,
            name=name,
            config=config,
        )

        custom_field.additional_properties = d
        return custom_field

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
