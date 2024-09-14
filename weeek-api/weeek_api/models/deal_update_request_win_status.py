from enum import Enum


class DealUpdateRequestWinStatus(str, Enum):
    ARCHIVED = "archived"
    LOST = "lost"
    WON = "won"

    def __str__(self) -> str:
        return str(self.value)
