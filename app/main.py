from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.database.base import Base
from app.database.fake_database import FakeDatabase

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest

from app.responses.notes_getting import NotesGettingResponse


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


def get_database() -> Base:
    return FakeDatabase()


database = get_database()
app = get_application()


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
