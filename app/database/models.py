from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from app.database.database_connection import DeclarativeBase


class Note(DeclarativeBase):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, nullable=False)
    topic = Column(String, nullable=False)
    content = Column(String, nullable=False)
