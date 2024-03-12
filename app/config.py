"""In this we create a special model to store settings"""

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Class to store various settings"""
    db_url: str = Field(..., env='DATABASE_URL')


settings = Settings()
