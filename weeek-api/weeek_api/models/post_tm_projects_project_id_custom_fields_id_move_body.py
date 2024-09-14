from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTmProjectsProjectIdCustomFieldsIdMoveBody")


@_attrs_define
class PostTmProjectsProjectIdCustomFieldsIdMoveBody:
    """
    Attributes:
        after (str): An custom field id after which should be moved. Cannot be provided together with before.
        before (str): An custom field id before which should be moved. Cannot be provided together with after.
    """

    after: str
    before: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after = self.after

        before = self.before

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after": after,
                "before": before,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = d.pop("after")

        before = d.pop("before")

        post_tm_projects_project_id_custom_fields_id_move_body = cls(
            after=after,
            before=before,
        )

        post_tm_projects_project_id_custom_fields_id_move_body.additional_properties = d
        return post_tm_projects_project_id_custom_fields_id_move_body

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
