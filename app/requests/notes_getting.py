from pydantic import BaseModel


class NotesGettingRequest(BaseModel):
    author_id: int
    offset: int
    count: int
