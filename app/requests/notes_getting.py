import attr


@attr.s
class NotesGettingRequest:
    author_id: int = attr.ib()
    offset: int = attr.ib()
    count: int = attr.ib()
