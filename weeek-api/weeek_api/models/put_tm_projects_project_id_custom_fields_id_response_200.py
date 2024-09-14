from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_field import CustomField


T = TypeVar("T", bound="PutTmProjectsProjectIdCustomFieldsIdResponse200")


@_attrs_define
class PutTmProjectsProjectIdCustomFieldsIdResponse200:
    """
    Attributes:
        success (bool):
        custom_field (CustomField):
    """

    success: bool
    custom_field: "CustomField"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        custom_field = self.custom_field.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "customField": custom_field,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field import CustomField

        d = src_dict.copy()
        success = d.pop("success")

        custom_field = CustomField.from_dict(d.pop("customField"))

        put_tm_projects_project_id_custom_fields_id_response_200 = cls(
            success=success,
            custom_field=custom_field,
        )

        put_tm_projects_project_id_custom_fields_id_response_200.additional_properties = d
        return put_tm_projects_project_id_custom_fields_id_response_200

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
