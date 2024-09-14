from enum import Enum


class CustomFieldOptionColor(str, Enum):
    BLUE = "blue"
    DARK_GREEN = "dark_green"
    DARK_PINK = "dark_pink"
    DARK_PURPLE = "dark_purple"
    DARK_YELLOW = "dark_yellow"
    GREEN = "green"
    LIGHT_BLUE = "light_blue"
    LIGHT_GREEN = "light_green"
    LIGHT_PINK = "light_pink"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"

    def __str__(self) -> str:
        return str(self.value)
