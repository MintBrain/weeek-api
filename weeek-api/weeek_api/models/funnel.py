import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField


T = TypeVar("T", bound="Funnel")


@_attrs_define
class Funnel:
    """
    Attributes:
        id (Union[Unset, str]):
        creator_id (Union[Unset, str]):
        currency_id (Union[Unset, int]):  Default: 1.
        name (Union[Unset, str]):
        logo (Union[None, Unset, str]):
        deals_count (Union[Unset, int]):
        deals_amount (Union[Unset, float]):
        is_private (Union[Unset, bool]):  Default: False.
        is_bookmarked (Union[Unset, bool]):  Default: False.
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        team (Union[Unset, List[str]]):
        custom_fields (Union[Unset, List['CustomField']]):
    """

    id: Union[Unset, str] = UNSET
    creator_id: Union[Unset, str] = UNSET
    currency_id: Union[Unset, int] = 1
    name: Union[Unset, str] = UNSET
    logo: Union[None, Unset, str] = UNSET
    deals_count: Union[Unset, int] = UNSET
    deals_amount: Union[Unset, float] = UNSET
    is_private: Union[Unset, bool] = False
    is_bookmarked: Union[Unset, bool] = False
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    team: Union[Unset, List[str]] = UNSET
    custom_fields: Union[Unset, List["CustomField"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        currency_id = self.currency_id

        name = self.name

        logo: Union[None, Unset, str]
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        deals_count = self.deals_count

        deals_amount = self.deals_amount

        is_private = self.is_private

        is_bookmarked = self.is_bookmarked

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        team: Union[Unset, List[str]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team

        custom_fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creator_id is not UNSET:
            field_dict["creatorId"] = creator_id
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if deals_count is not UNSET:
            field_dict["dealsCount"] = deals_count
        if deals_amount is not UNSET:
            field_dict["dealsAmount"] = deals_amount
        if is_private is not UNSET:
            field_dict["isPrivate"] = is_private
        if is_bookmarked is not UNSET:
            field_dict["isBookmarked"] = is_bookmarked
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if team is not UNSET:
            field_dict["team"] = team
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field import CustomField

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        creator_id = d.pop("creatorId", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo = _parse_logo(d.pop("logo", UNSET))

        deals_count = d.pop("dealsCount", UNSET)

        deals_amount = d.pop("dealsAmount", UNSET)

        is_private = d.pop("isPrivate", UNSET)

        is_bookmarked = d.pop("isBookmarked", UNSET)

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

        team = cast(List[str], d.pop("team", UNSET))

        custom_fields = []
        _custom_fields = d.pop("customFields", UNSET)
        for custom_fields_item_data in _custom_fields or []:
            custom_fields_item = CustomField.from_dict(custom_fields_item_data)

            custom_fields.append(custom_fields_item)

        funnel = cls(
            id=id,
            creator_id=creator_id,
            currency_id=currency_id,
            name=name,
            logo=logo,
            deals_count=deals_count,
            deals_amount=deals_amount,
            is_private=is_private,
            is_bookmarked=is_bookmarked,
            created_at=created_at,
            updated_at=updated_at,
            team=team,
            custom_fields=custom_fields,
        )

        funnel.additional_properties = d
        return funnel

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
