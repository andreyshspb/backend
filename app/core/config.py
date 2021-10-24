
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Project"

    DATABASE_URI: str = "postgresql://postgres:secret@0.0.0.0:5432/notes"
    TEST_DATABASE_URI: str = "postgresql://postgres:secret@0.0.0.0:5432/notes"

    MESSAGE_BROKER_HOST = "0.0.0.0"
    MESSAGE_BROKER_PORT = 5672


settings = Settings()
