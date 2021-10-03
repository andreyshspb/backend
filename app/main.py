from fastapi import FastAPI

from app.core.config import settings

from app.database.base import Base
from app.database.in_memory_database import InMemoryDatabase

from app.restapi import start_restapi


def get_application():
    return FastAPI(title=settings.PROJECT_NAME)


def get_database() -> Base:
    return InMemoryDatabase()


database = get_database()
app = get_application()


start_restapi(app, database)
