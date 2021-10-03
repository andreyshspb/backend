from pydantic import BaseModel


class NoteEditingRequest(BaseModel):
    note_id: int
    new_topic: str
    new_content: str
