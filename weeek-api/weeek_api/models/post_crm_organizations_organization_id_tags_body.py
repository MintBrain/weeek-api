from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostCrmOrganizationsOrganizationIdTagsBody")


@_attrs_define
class PostCrmOrganizationsOrganizationIdTagsBody:
    """
    Attributes:
        tag_id (int):
    """

    tag_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_id = self.tag_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagId": tag_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_id = d.pop("tagId")

        post_crm_organizations_organization_id_tags_body = cls(
            tag_id=tag_id,
        )

        post_crm_organizations_organization_id_tags_body.additional_properties = d
        return post_crm_organizations_organization_id_tags_body

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
