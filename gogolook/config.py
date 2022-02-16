from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    DATABASE_URI: str
    LOG_LEVEL: str = "info"

    @validator("LOG_LEVEL", allow_reuse=True)
    def get_log_level(cls, v: str) -> str:
        return v.lower()
