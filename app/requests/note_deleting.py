from pydantic import BaseModel


class NoteDeletingRequest(BaseModel):
    note_id: int
