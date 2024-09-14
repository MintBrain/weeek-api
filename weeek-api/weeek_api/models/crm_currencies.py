from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="CrmCurrencies")


@_attrs_define
class CrmCurrencies:
    """
    Attributes:
        success (Union[Unset, bool]):
        currencies (Union[Unset, List['Currency']]):
    """

    success: Union[Unset, bool] = UNSET
    currencies: Union[Unset, List["Currency"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        currencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()
                currencies.append(currencies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if currencies is not UNSET:
            field_dict["currencies"] = currencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.currency import Currency

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = Currency.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        crm_currencies = cls(
            success=success,
            currencies=currencies,
        )

        crm_currencies.additional_properties = d
        return crm_currencies

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
