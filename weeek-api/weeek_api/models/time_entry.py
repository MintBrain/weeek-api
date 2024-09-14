import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.time_entry_type import TimeEntryType

T = TypeVar("T", bound="TimeEntry")


@_attrs_define
class TimeEntry:
    """
    Attributes:
        id (str):
        user_id (str):
        type (TimeEntryType):
        is_overtime (bool): A flag indicating that the entry was overtime
        date (datetime.date): The day of entry. In `Y-m-d` format
        duration (int): Time in minutes, cannot exceed 1440
    """

    id: str
    user_id: str
    type: TimeEntryType
    is_overtime: bool
    date: datetime.date
    duration: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        type = self.type.value

        is_overtime = self.is_overtime

        date = self.date.isoformat()

        duration = self.duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "userId": user_id,
                "type": type,
                "isOvertime": is_overtime,
                "date": date,
                "duration": duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("userId")

        type = TimeEntryType(d.pop("type"))

        is_overtime = d.pop("isOvertime")

        date = isoparse(d.pop("date")).date()

        duration = d.pop("duration")

        time_entry = cls(
            id=id,
            user_id=user_id,
            type=type,
            is_overtime=is_overtime,
            date=date,
            duration=duration,
        )

        time_entry.additional_properties = d
        return time_entry

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
