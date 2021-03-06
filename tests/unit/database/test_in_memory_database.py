import pytest

from app.database.in_memory_database import InMemoryDatabase

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest


# create_note() method

def test_create_one_note():
    database = InMemoryDatabase()

    request = NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Watch the last lecture"
    )
    database.create_note(request)

    assert len(database.notes) == 1
    assert database.next_note_id == 1

    assert database.notes[0]["note_id"] == 0
    assert database.notes[0]["author_id"] == 1
    assert database.notes[0]["topic"] == "Math statistics"
    assert database.notes[0]["content"] == "Watch the last lecture"


def test_create_two_note_with_different_authors():
    database = InMemoryDatabase()

    request = NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Watch the last lecture"
    )
    database.create_note(request)
    request = NoteCreationRequest(
        author_id=2,
        topic="HSE",
        content="It is my university"
    )
    database.create_note(request)

    assert len(database.notes) == 2
    assert database.next_note_id == 2

    assert database.notes[0]["note_id"] == 0
    assert database.notes[0]["author_id"] == 1
    assert database.notes[0]["topic"] == "Math statistics"
    assert database.notes[0]["content"] == "Watch the last lecture"

    assert database.notes[1]["note_id"] == 1
    assert database.notes[1]["author_id"] == 2
    assert database.notes[1]["topic"] == "HSE"
    assert database.notes[1]["content"] == "It is my university"


def test_create_two_note_with_the_same_author():
    database = InMemoryDatabase()

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Math statistics",
        content="Do nothing"
    ))
    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="HSE",
        content="It is my university"
    ))

    assert len(database.notes) == 2
    assert database.next_note_id == 2

    assert database.notes[0]["note_id"] == 0
    assert database.notes[0]["author_id"] == 1
    assert database.notes[0]["topic"] == "Math statistics"
    assert database.notes[0]["content"] == "Do nothing"

    assert database.notes[1]["note_id"] == 1
    assert database.notes[1]["author_id"] == 1
    assert database.notes[1]["topic"] == "HSE"
    assert database.notes[1]["content"] == "It is my university"


# get_notes() method

def test_get_notes_from_empty_database():
    database = InMemoryDatabase()
    request = NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    )
    response = database.get_notes(request)
    assert len(response.notes) == 0
    assert len(database.notes) == 0
    assert database.next_note_id == 0


def test_get_notes():
    database = InMemoryDatabase()

    first = NoteCreationRequest(
        author_id=1,
        topic="First",
        content=""
    )
    second = NoteCreationRequest(
        author_id=1,
        topic="Second",
        content=""
    )
    third = NoteCreationRequest(
        author_id=2,
        topic="Math statistics",
        content=""
    )
    database.create_note(first)
    database.create_note(second)
    database.create_note(third)

    request = NotesGettingRequest(
        author_id=1,
        offset=0,
        count=10
    )
    response = database.get_notes(request)

    assert len(response.notes) == 2

    assert response.notes[0].author_id == 1
    assert response.notes[0].topic == "First"
    assert response.notes[1].author_id == 1
    assert response.notes[1].topic == "Second"


def test_get_notes_with_count():
    database = InMemoryDatabase()

    first = NoteCreationRequest(
        author_id=1,
        topic="First",
        content=""
    )
    second = NoteCreationRequest(
        author_id=1,
        topic="Second",
        content=""
    )
    database.create_note(first)
    database.create_note(second)

    request = NotesGettingRequest(
        author_id=1,
        offset=0,
        count=1
    )
    response = database.get_notes(request)

    assert len(response.notes) == 1

    assert response.notes[0].author_id == 1
    assert response.notes[0].topic == "First"


# delete_note() method

def test_delete_one_note():
    database = InMemoryDatabase()

    first = NoteCreationRequest(
        author_id=1,
        topic="First",
        content=""
    )
    second = NoteCreationRequest(
        author_id=2,
        topic="Second",
        content="Hello world"
    )
    database.create_note(first)
    database.create_note(second)

    request = NoteDeletingRequest(
        note_id=0
    )
    database.delete_note(request)

    assert len(database.notes) == 1
    assert database.next_note_id == 2

    assert database.notes[0]["author_id"] == 2
    assert database.notes[0]["topic"] == "Second"
    assert database.notes[0]["content"] == "Hello world"


def test_double_delete():
    database = InMemoryDatabase()

    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="Statistics",
        content="Watch seminar"
    ))

    database.delete_note(NoteDeletingRequest(
        note_id=0
    ))

    try:
        database.delete_note(NoteDeletingRequest(
            note_id=0
        ))
    except Exception as exception:
        pytest.fail("Unexpected error:\n" + str(exception))

    assert len(database.notes) == 0
    assert database.next_note_id == 1


def test_delete_from_empty_database():
    database = InMemoryDatabase()

    try:
        database.delete_note(NoteDeletingRequest(
            note_id=0
        ))
    except Exception as exception:
        pytest.fail("Unexpected error:\n" + str(exception))

    assert len(database.notes) == 0
    assert database.next_note_id == 0


# edit_note() method

def test_edit_note():
    database = InMemoryDatabase()

    first = NoteCreationRequest(
        author_id=1,
        topic="First",
        content="Hello World"
    )
    second = NoteCreationRequest(
        author_id=1,
        topic="Third",
        content="What???"
    )
    database.create_note(first)
    database.create_note(second)

    request = NoteEditingRequest(
        note_id=0,
        new_topic="Second",
        new_content="Hello Python"
    )
    database.edit_note(request)

    assert len(database.notes) == 2
    assert database.next_note_id == 2

    assert database.notes[0]["note_id"] == 0
    assert database.notes[0]["author_id"] == 1
    assert database.notes[0]["topic"] == "Second"
    assert database.notes[0]["content"] == "Hello Python"

    assert database.notes[1]["note_id"] == 1
    assert database.notes[1]["author_id"] == 1
    assert database.notes[1]["topic"] == "Third"
    assert database.notes[1]["content"] == "What???"


def test_edit_in_empty_database():
    database = InMemoryDatabase()

    try:
        database.edit_note(NoteEditingRequest(
            note_id=0,
            new_topic="HSE",
            new_content="It is my university"
        ))
    except Exception as exception:
        pytest.fail("Unexpected error:\n" + str(exception))

    assert len(database.notes) == 0
    assert database.next_note_id == 0


def test_double_editing_note():
    database = InMemoryDatabase()
    database.create_note(NoteCreationRequest(
        author_id=1,
        topic="HSE",
        content="It is my university"
    ))

    database.edit_note(NoteEditingRequest(
        note_id=0,
        new_topic="Python",
        new_content="Do Homework"
    ))
    database.edit_note(NoteEditingRequest(
        note_id=0,
        new_topic="ML",
        new_content="Watch the last lecture"
    ))

    assert len(database.notes) == 1
    assert database.next_note_id == 1

    assert database.notes[0]["note_id"] == 0
    assert database.notes[0]["author_id"] == 1
    assert database.notes[0]["topic"] == "ML"
    assert database.notes[0]["content"] == "Watch the last lecture"
