
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Project"


settings = Settings()
