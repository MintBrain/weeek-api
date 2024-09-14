from enum import Enum


class PostTmTasksBodyType(str, Enum):
    ACTION = "action"
    CALL = "call"
    MEET = "meet"

    def __str__(self) -> str:
        return str(self.value)
