import attr

from typing import List


@attr.s
class NoteDescription:
    author_id: int = attr.ib()
    topic: str = attr.ib()


@attr.s
class NotesGettingResponse:
    notes: List[NoteDescription] = attr.ib()
