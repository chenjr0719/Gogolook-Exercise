from logging import Logger

from pytest import Session

from gogolook.models import Task, TaskSchema, TaskUpdateSchema
from gogolook.services import CRUDService


class TaskCRUDService(CRUDService):
    pass


def get_task_service(session: Session, logger: Logger):  # noqa
    task_service = TaskCRUDService(
        model=Task,
        schema=TaskSchema,
        session=session,
        logger=logger,
        update_schema=TaskUpdateSchema,
    )

    return task_service
