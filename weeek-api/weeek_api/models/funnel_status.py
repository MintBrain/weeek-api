import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunnelStatus")


@_attrs_define
class FunnelStatus:
    """
    Attributes:
        id (Union[Unset, str]):
        creator_id (Union[Unset, str]):
        name (Union[Unset, str]):
        deals_count (Union[Unset, int]):
        deals_amount (Union[Unset, float]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    deals_count: Union[Unset, int] = UNSET
    deals_amount: Union[Unset, float] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        name = self.name

        deals_count = self.deals_count

        deals_amount = self.deals_amount

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if name is not UNSET:
            field_dict["name"] = name
        if deals_count is not UNSET:
            field_dict["dealsCount"] = deals_count
        if deals_amount is not UNSET:
            field_dict["dealsAmount"] = deals_amount
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        name = d.pop("name", UNSET)

        deals_count = d.pop("dealsCount", UNSET)

        deals_amount = d.pop("dealsAmount", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        funnel_status = cls(
            id=id,
            creator_id=creator_id,
            name=name,
            deals_count=deals_count,
            deals_amount=deals_amount,
            created_at=created_at,
            updated_at=updated_at,
        )

        funnel_status.additional_properties = d
        return funnel_status

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
