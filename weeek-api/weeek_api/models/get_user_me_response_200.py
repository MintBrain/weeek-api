from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_user import CurrentUser


T = TypeVar("T", bound="GetUserMeResponse200")


@_attrs_define
class GetUserMeResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        user (Union[Unset, CurrentUser]):
    """

    success: Union[Unset, bool] = UNSET
    user: Union[Unset, "CurrentUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.current_user import CurrentUser

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _user = d.pop("user", UNSET)
        user: Union[Unset, CurrentUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = CurrentUser.from_dict(_user)

        get_user_me_response_200 = cls(
            success=success,
            user=user,
        )

        get_user_me_response_200.additional_properties = d
        return get_user_me_response_200

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
