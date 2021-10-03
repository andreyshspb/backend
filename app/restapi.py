from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest

from app.responses.notes_getting import NotesGettingResponse


def start_restapi(app, database):

    @app.post("/get/notes/")
    async def get_notes(request: NotesGettingRequest) -> NotesGettingResponse:
        return database.get_notes(request)

    @app.post("/create/note")
    async def create_note(request: NoteCreationRequest) -> None:
        return database.create_note(request)

    @app.post("/delete/note")
    async def delete_note(request: NoteDeletingRequest) -> None:
        return database.delete_note(request)

    @app.post("/edit/note")
    async def edit_note(request: NoteEditingRequest) -> None:
        return database.edit_note(request)