from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.board_column import BoardColumn


T = TypeVar("T", bound="GetTmBoardColumnsResponse200")


@_attrs_define
class GetTmBoardColumnsResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):
        board_columns (Union[Unset, List['BoardColumn']]):
    """

    success: Union[Unset, bool] = UNSET
    board_columns: Union[Unset, List["BoardColumn"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        board_columns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.board_columns, Unset):
            board_columns = []
            for board_columns_item_data in self.board_columns:
                board_columns_item = board_columns_item_data.to_dict()
                board_columns.append(board_columns_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if board_columns is not UNSET:
            field_dict["boardColumns"] = board_columns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.board_column import BoardColumn

        d = src_dict.copy()
        success = d.pop("success", UNSET)

        board_columns = []
        _board_columns = d.pop("boardColumns", UNSET)
        for board_columns_item_data in _board_columns or []:
            board_columns_item = BoardColumn.from_dict(board_columns_item_data)

            board_columns.append(board_columns_item)

        get_tm_board_columns_response_200 = cls(
            success=success,
            board_columns=board_columns,
        )

        get_tm_board_columns_response_200.additional_properties = d
        return get_tm_board_columns_response_200

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
