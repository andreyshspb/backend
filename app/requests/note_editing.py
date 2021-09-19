import attr


@attr.s
class NoteEditingRequest:
    note_id: int = attr.ib()
    new_topic: str = attr.ib()
    new_content: str = attr.ib()
