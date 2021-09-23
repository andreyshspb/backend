import attr

from pydantic import BaseModel


@attr.s
class NotesGettingRequest(BaseModel):
    author_id: int = attr.ib()
    offset: int = attr.ib()
    count: int = attr.ib()
