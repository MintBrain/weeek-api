from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deal_update_request_win_status import DealUpdateRequestWinStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_values import CustomFieldValues


T = TypeVar("T", bound="DealUpdateRequest")


@_attrs_define
class DealUpdateRequest:
    """
    Attributes:
        title (Union[None, Unset, str]):
        amount (Union[None, Unset, float]):
        win_status (Union[Unset, DealUpdateRequestWinStatus]):
        custom_fields (Union[Unset, CustomFieldValues]): A key-value object with custom field id as key and custom field
            value

            For example

            ```
            "customFields" : {
                "<text_custom_field_id>": "Text value",
                "<boolean_custom_field_id>": true,
                "<datetime_custom_field_id>": "<ISO 8601 datetime string>",
                "<select_custom_field_id>": "<custom_field_option_id>"
                "<multiselect_custom_field_id>": ["<custom_field_option_id>"],
                "<member_custom_field_id>": ["<user_id>"],
                "<contact_custom_field_id>": "<contact_id>",
                "<link_custom_field_id>": "https://example.com",
                "<approval_custom_field_id>": ["<user_id>"]
            }
            ```
    """

    title: Union[None, Unset, str] = UNSET
    amount: Union[None, Unset, float] = UNSET
    win_status: Union[Unset, DealUpdateRequestWinStatus] = UNSET
    custom_fields: Union[Unset, "CustomFieldValues"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        amount: Union[None, Unset, float]
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        win_status: Union[Unset, str] = UNSET
        if not isinstance(self.win_status, Unset):
            win_status = self.win_status.value

        custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if amount is not UNSET:
            field_dict["amount"] = amount
        if win_status is not UNSET:
            field_dict["winStatus"] = win_status
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_values import CustomFieldValues

        d = src_dict.copy()

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        amount = _parse_amount(d.pop("amount", UNSET))

        _win_status = d.pop("winStatus", UNSET)
        win_status: Union[Unset, DealUpdateRequestWinStatus]
        if isinstance(_win_status, Unset):
            win_status = UNSET
        else:
            win_status = DealUpdateRequestWinStatus(_win_status)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CustomFieldValues]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CustomFieldValues.from_dict(_custom_fields)

        deal_update_request = cls(
            title=title,
            amount=amount,
            win_status=win_status,
            custom_fields=custom_fields,
        )

        deal_update_request.additional_properties = d
        return deal_update_request

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
