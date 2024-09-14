from enum import Enum


class AttachmentServiceEnum(str, Enum):
    BOX = "box"
    DROPBOX = "dropbox"
    GOOGLE_DRIVE = "google_drive"
    ONE_DRIVE = "one_drive"
    WEEEK = "weeek"

    def __str__(self) -> str:
        return str(self.value)
