from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.funnel import Funnel


T = TypeVar("T", bound="CrmFunnel")


@_attrs_define
class CrmFunnel:
    """
    Attributes:
        success (Union[Unset, bool]):
        funnel (Union[Unset, Funnel]):
    """

    success: Union[Unset, bool] = UNSET
    funnel: Union[Unset, "Funnel"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        funnel: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.funnel, Unset):
            funnel = self.funnel.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if funnel is not UNSET:
            field_dict["funnel"] = funnel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.funnel import Funnel

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _funnel = d.pop("funnel", UNSET)
        funnel: Union[Unset, Funnel]
        if isinstance(_funnel, Unset):
            funnel = UNSET
        else:
            funnel = Funnel.from_dict(_funnel)

        crm_funnel = cls(
            success=success,
            funnel=funnel,
        )

        crm_funnel.additional_properties = d
        return crm_funnel

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
