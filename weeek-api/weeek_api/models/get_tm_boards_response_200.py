from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board import Board


T = TypeVar("T", bound="GetTmBoardsResponse200")


@_attrs_define
class GetTmBoardsResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        boards (Union[Unset, List['Board']]):
    """

    success: Union[Unset, bool] = UNSET
    boards: Union[Unset, List["Board"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        boards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.boards, Unset):
            boards = []
            for boards_item_data in self.boards:
                boards_item = boards_item_data.to_dict()
                boards.append(boards_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if boards is not UNSET:
            field_dict["boards"] = boards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.board import Board

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        boards = []
        _boards = d.pop("boards", UNSET)
        for boards_item_data in _boards or []:
            boards_item = Board.from_dict(boards_item_data)

            boards.append(boards_item)

        get_tm_boards_response_200 = cls(
            success=success,
            boards=boards,
        )

        get_tm_boards_response_200.additional_properties = d
        return get_tm_boards_response_200

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
