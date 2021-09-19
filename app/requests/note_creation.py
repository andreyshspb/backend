import attr


@attr.s
class NoteCreationRequest:
    author_id: int = attr.ib()
    topic: str = attr.ib()
    content: str = attr.ib()
