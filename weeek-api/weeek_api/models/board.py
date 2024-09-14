from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Board")


@_attrs_define
class Board:
    """
    Attributes:
        id (int):
        name (str):
        project_id (int):
        is_private (bool):
    """

    id: int
    name: str
    project_id: int
    is_private: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        project_id = self.project_id

        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "projectId": project_id,
                "isPrivate": is_private,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        project_id = d.pop("projectId")

        is_private = d.pop("isPrivate")

        board = cls(
            id=id,
            name=name,
            project_id=project_id,
            is_private=is_private,
        )

        board.additional_properties = d
        return board

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
