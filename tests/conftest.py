import pytest

from gogolook.config import Settings
from gogolook.db import get_session
from gogolook.logger import get_logger
from gogolook.services import get_task_service


@pytest.fixture()
def mock_settings():
    settings = Settings()

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


@pytest.fixture()
def mock_task_service(mock_db_session, mock_logger):
    task_service = get_task_service(session=mock_db_session, logger=mock_logger)
    yield task_service

    # Clean up
    tasks = task_service.list()
    for task in tasks:
        task_service.delete(db_obj=task)


@pytest.fixture()
def dummy_tasks(mock_task_service):
    tasks = [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
    tasks = [mock_task_service.create(obj=task) for task in tasks]

    return tasks
