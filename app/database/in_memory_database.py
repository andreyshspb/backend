from typing import List, NoReturn

from app.database.base import Base

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest

from app.responses.notes_getting import NoteDescription
from app.responses.notes_getting import NotesGettingResponse


class InMemoryDatabase(Base):

    def __init__(self):
        self.notes = [
            {
                "note_id": 0,
                "author_id": 0,
                "topic": "Math",
                "content": "Watch Lecture"
            },
            {
                "note_id": 1,
                "author_id": 0,
                "topic": "ML",
                "content": "Test Preparation"
            }
        ]
        self.next_note_id = len(self.notes)

    def get_notes(self, request: NotesGettingRequest) -> NotesGettingResponse:
        result: List[NoteDescription] = []
        for note in self.notes:
            if note["author_id"] == request.author_id:
                result.append(NoteDescription(note["author_id"], note["topic"]))
        return NotesGettingResponse(result[request.offset:][:request.count])

    def create_note(self, request: NoteCreationRequest) -> NoReturn:
        self.notes.append({
            "note_id": self.next_note_id,
            "author_id": request.author_id,
            "topic": request.topic,
            "content": request.content
        })
        self.next_note_id += 1

    def delete_note(self, request: NoteDeletingRequest) -> NoReturn:
        for i in range(len(self.notes)):
            if self.notes[i]["note_id"] == request.note_id:
                self.notes.pop(i)
                return

    def edit_note(self, request: NoteEditingRequest) -> NoReturn:
        for note in self.notes:
            if note["note_id"] == request.note_id:
                note["topic"] = request.new_topic
                note["content"] = request.new_content
                return
