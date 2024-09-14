from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostCrmDealsDealIdAssigneesBody")


@_attrs_define
class PostCrmDealsDealIdAssigneesBody:
    """
    Attributes:
        assignee_id (str):
    """

    assignee_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assignee_id = self.assignee_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assigneeId": assignee_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        assignee_id = d.pop("assigneeId")

        post_crm_deals_deal_id_assignees_body = cls(
            assignee_id=assignee_id,
        )

        post_crm_deals_deal_id_assignees_body.additional_properties = d
        return post_crm_deals_deal_id_assignees_body

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
