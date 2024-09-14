from enum import Enum


class CustomFieldCreateBodyType(str, Enum):
    APPROVAL = "approval"
    BOOLEAN = "boolean"
    CONTACT = "contact"
    DATETIME = "datetime"
    LINK = "link"
    MEMBER = "member"
    MULTISELECT = "multiselect"
    SELECT = "select"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
