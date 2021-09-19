import attr


@attr.s
class NoteDeletingRequest:
    note_id: int = attr.ib()
