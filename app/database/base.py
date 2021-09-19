from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest

from app.responses.notes_getting import NotesGettingResponse


class Base:

    def get_notes(self, request: NotesGettingRequest) -> NotesGettingResponse:
        raise NotImplementedError

    def create_note(self, request: NoteCreationRequest) -> None:
        raise NotImplementedError

    def delete_note(self, request: NoteDeletingRequest) -> None:
        raise NotImplementedError

    def edit_note(self, request: NoteEditingRequest) -> None:
        raise NotImplementedError
