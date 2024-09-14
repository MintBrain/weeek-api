from enum import Enum


class DealCreateRequestWinStatus(str, Enum):
    ARCHIVED = "archived"
    LOST = "lost"
    WON = "won"

    def __str__(self) -> str:
        return str(self.value)
