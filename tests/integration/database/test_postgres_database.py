from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


from app.database.postgres_database import PostgresDatabase

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest


engine = create_engine(settings.TEST_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DeclarativeBase = declarative_base()


def test_get_right_notes():
    database = PostgresDatabase(SessionLocal)

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Statistics",
        content="Watch the last lecture"
    ))
    database.create_note(NoteCreationRequest(
        author_id=2,
        topic="HSE University",
        content="It is my university"
    ))
    response = database.get_notes(NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    ))

    notes = response.notes
    assert len(notes) == 1
    assert notes[0].author_id == 1
    assert notes[0].topic == "Statistics"
