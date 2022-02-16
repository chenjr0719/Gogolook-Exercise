import pytest

from gogolook.config import Settings
from gogolook.db import get_session
from gogolook.logger import get_logger


@pytest.fixture()
def mock_settings():
    settings = Settings()
    settings.DATABASE_URI = "sqlite:///:memory:"
    settings.LOG_LEVEL = "debug"

    return settings


@pytest.fixture()
def mock_db_session(mock_settings):
    db_session = get_session(mock_settings)

    from gogolook.models import Base

    Base.metadata.create_all(bind=db_session.get_bind())

    return db_session


@pytest.fixture()
def mock_logger(mock_settings):
    logger = get_logger(mock_settings)

    return logger
