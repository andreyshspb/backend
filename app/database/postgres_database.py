from sqlalchemy.orm import Session

from app.database.base import Base

from app.requests.notes_getting import NotesGettingRequest
from app.requests.note_creation import NoteCreationRequest
from app.requests.note_deleting import NoteDeletingRequest
from app.requests.note_editing import NoteEditingRequest

from app.responses.notes_getting import NoteDescription
from app.responses.notes_getting import NotesGettingResponse

from app.database.models import Note


class PostgresDatabase(Base):

    def __init__(self, session_maker):
        self.session_maker = session_maker

    def get_notes(self, request: NotesGettingRequest) -> NotesGettingResponse:
        database: Session = self.session_maker()
        notes = database.query(Note)\
            .filter(Note.author_id == request.author_id)\
            .offset(request.offset)\
            .limit(request.count)
        description = []
        for note in notes:
            description.append(NoteDescription(note.author_id, note.topic))
        return NotesGettingResponse(description)

    def create_note(self, request: NoteCreationRequest) -> None:
        database: Session = self.session_maker()
        new_note = Note(
            author_id=request.author_id,
            topic=request.topic,
            content=request.content
        )
        database.add(new_note)
        database.commit()

    def delete_note(self, request: NoteDeletingRequest) -> None:
        database: Session = self.session_maker()
        database.query(Note).filter(Note.id == request.note_id).delete()
        database.commit()

    def edit_note(self, request: NoteEditingRequest) -> None:
        database: Session = self.session_maker()
        note = database.query(Note).filter(Note.id == request.note_id).first()
        if note:
            note.topic = request.new_topic
            note.content = request.new_content
        database.commit()
