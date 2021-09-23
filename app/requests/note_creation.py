import attr

from pydantic import BaseModel


@attr.s
class NoteCreationRequest(BaseModel):
    author_id: int = attr.ib()
    topic: str = attr.ib()
    content: str = attr.ib()
