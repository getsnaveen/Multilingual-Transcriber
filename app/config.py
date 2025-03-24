from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from functools import lru_cache

class AppSettings(BaseSettings):
    app_name: str = "Multilingual Transcriber"
    OPENAI_API_KEY: str = Field(default="None", env= "OPENAI_API_KEY")
    FILEPATH: str = Field(default="None", env= "FILEPATH")

@lru_cache
def get_settings():
    settings = AppSettings()
    return settings