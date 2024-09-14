from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field_option import CustomFieldOption


T = TypeVar("T", bound="PutCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200")


@_attrs_define
class PutCrmFunnelsFunnelIdCustomFieldsCustomFieldIdOptionsIdResponse200:
    """
    Attributes:
        success (bool):
        option (CustomFieldOption):
    """

    success: bool
    option: "CustomFieldOption"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        option = self.option.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "option": option,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_option import CustomFieldOption

        d = src_dict.copy()
        success = d.pop("success")

        option = CustomFieldOption.from_dict(d.pop("option"))

        put_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_response_200 = cls(
            success=success,
            option=option,
        )

        put_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_response_200.additional_properties = d
        return put_crm_funnels_funnel_id_custom_fields_custom_field_id_options_id_response_200

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
