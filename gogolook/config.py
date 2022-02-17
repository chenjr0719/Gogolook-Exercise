from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    DATABASE_URI: str = "sqlite:///:memory:"
    LOG_LEVEL: str = "info"

    @validator("LOG_LEVEL", allow_reuse=True)
    def get_log_level(cls, v: str) -> str:
        return v.lower()

    AUTO_MIGRATE: bool = True
