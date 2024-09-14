from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostTmBoardsIdMoveBody")


@_attrs_define
class PostTmBoardsIdMoveBody:
    """
    Attributes:
        upper_board_id (Union[None, int]):
    """

    upper_board_id: Union[None, int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        upper_board_id: Union[None, int]
        upper_board_id = self.upper_board_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upperBoardId": upper_board_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_upper_board_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        upper_board_id = _parse_upper_board_id(d.pop("upperBoardId"))

        post_tm_boards_id_move_body = cls(
            upper_board_id=upper_board_id,
        )

        post_tm_boards_id_move_body.additional_properties = d
        return post_tm_boards_id_move_body

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
