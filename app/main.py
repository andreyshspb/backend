from fastapi import FastAPI

from app.core.config import settings

from app.database.base import Base
from app.database.postgres_database import PostgresDatabase
from app.database.database_connection import SessionLocal

from app.restapi import start_restapi
from app.graphql import start_graphql


def get_application():
    return FastAPI(title=settings.PROJECT_NAME)


def get_database() -> Base:
    return PostgresDatabase(session_maker=SessionLocal)


database = get_database()
app = get_application()


start_restapi(app, database)
start_graphql(app, database)
