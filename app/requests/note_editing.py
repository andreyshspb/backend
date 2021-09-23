import attr

from pydantic import BaseModel


@attr.s
class NoteEditingRequest(BaseModel):
    note_id: int = attr.ib()
    new_topic: str = attr.ib()
    new_content: str = attr.ib()
