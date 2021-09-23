import attr

from pydantic import BaseModel


@attr.s
class NoteDeletingRequest(BaseModel):
    note_id: int = attr.ib()
