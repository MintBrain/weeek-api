from enum import Enum


class CustomFieldValueConfigType0Type(str, Enum):
    CHECKBOX = "checkbox"
    SWITCH = "switch"

    def __str__(self) -> str:
        return str(self.value)
