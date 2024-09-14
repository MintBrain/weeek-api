from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_column import BoardColumn


T = TypeVar("T", bound="PostTmBoardColumnsResponse200")


@_attrs_define
class PostTmBoardColumnsResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        board_column (Union[Unset, BoardColumn]):
    """

    success: Union[Unset, bool] = UNSET
    board_column: Union[Unset, "BoardColumn"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        board_column: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.board_column, Unset):
            board_column = self.board_column.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if board_column is not UNSET:
            field_dict["boardColumn"] = board_column

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.board_column import BoardColumn

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        _board_column = d.pop("boardColumn", UNSET)
        board_column: Union[Unset, BoardColumn]
        if isinstance(_board_column, Unset):
            board_column = UNSET
        else:
            board_column = BoardColumn.from_dict(_board_column)

        post_tm_board_columns_response_200 = cls(
            success=success,
            board_column=board_column,
        )

        post_tm_board_columns_response_200.additional_properties = d
        return post_tm_board_columns_response_200

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
