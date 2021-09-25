import pytest

from app.database.in_memory_database import InMemoryDatabase

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest


def test_note_cycle_life():
    database = InMemoryDatabase()

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Watch the last lecture"
    ))
    response = database.get_notes(NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    ))

    notes = response.notes
    assert len(notes) == 1
    assert notes[0].author_id == 1
    assert notes[0].topic == "Math statistics"

    database.edit_note(NoteEditingRequest(
        note_id=0,
        new_topic="ML",
        new_content="Do Homework"
    ))
    response = database.get_notes(NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    ))

    notes = response.notes
    assert len(notes) == 1
    assert notes[0].author_id == 1
    assert notes[0].topic == "ML"

    database.delete_note(NoteDeletingRequest(
        note_id=0
    ))
    response = database.get_notes(NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    ))

    notes = response.notes
    assert len(notes) == 0


def test_editing_after_deleting():
    database = InMemoryDatabase()

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Watch the last lecture"
    ))
    database.delete_note(NoteDeletingRequest(
        note_id=0
    ))

    try:
        database.edit_note(NoteEditingRequest(
            note_id=0,
            new_topic="ML",
            new_content="Do Homework"
        ))
    except Exception as exception:
        pytest.fail("Unexpected error:\n" + str(exception))

    response = database.get_notes(NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    ))

    notes = response.notes
    assert len(notes) == 0


def test_get_right_notes():
    database = InMemoryDatabase()

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Watch the last lecture"
    ))
    database.create_note(NoteCreationRequest(
        author_id=2,
        topic="HSE",
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
    assert notes[0].topic == "Math statistics"
