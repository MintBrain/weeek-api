from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTmTasksIdBoardColumnBody")


@_attrs_define
class PostTmTasksIdBoardColumnBody:
    """
    Attributes:
        board_column_id (int):
    """

    board_column_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        board_column_id = self.board_column_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boardColumnId": board_column_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        board_column_id = d.pop("boardColumnId")

        post_tm_tasks_id_board_column_body = cls(
            board_column_id=board_column_id,
        )

        post_tm_tasks_id_board_column_body.additional_properties = d
        return post_tm_tasks_id_board_column_body

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
