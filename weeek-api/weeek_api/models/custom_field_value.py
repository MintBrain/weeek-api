from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_value_type import CustomFieldValueType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_option import CustomFieldOption
    from ..models.custom_field_value_config_type_0 import CustomFieldValueConfigType0


T = TypeVar("T", bound="CustomFieldValue")


@_attrs_define
class CustomFieldValue:
    """
    Attributes:
        type (CustomFieldValueType):
        options (List['CustomFieldOption']): Only for select and multiselect custom fields
        value (str):
        id (Union[Unset, str]):
        name (Union[None, Unset, str]):
        config (Union['CustomFieldValueConfigType0', None, Unset]):
    """

    type: CustomFieldValueType
    options: List["CustomFieldOption"]
    value: str
    id: Union[Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    config: Union["CustomFieldValueConfigType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.custom_field_value_config_type_0 import CustomFieldValueConfigType0

        type = self.type.value

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        value = self.value

        id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        config: Union[Dict[str, Any], None, Unset]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, CustomFieldValueConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "options": options,
                "value": value,
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
        from ..models.custom_field_option import CustomFieldOption
        from ..models.custom_field_value_config_type_0 import CustomFieldValueConfigType0

        d = src_dict.copy()
        type = CustomFieldValueType(d.pop("type"))

        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = CustomFieldOption.from_dict(options_item_data)

            options.append(options_item)

        value = d.pop("value")

        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_config(data: object) -> Union["CustomFieldValueConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = CustomFieldValueConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CustomFieldValueConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        custom_field_value = cls(
            type=type,
            options=options,
            value=value,
            id=id,
            name=name,
            config=config,
        )

        custom_field_value.additional_properties = d
        return custom_field_value

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
