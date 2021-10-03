from pydantic import BaseModel


class NoteCreationRequest(BaseModel):
    author_id: int
    topic: str
    content: str
