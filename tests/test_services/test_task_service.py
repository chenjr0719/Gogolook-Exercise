import pytest

from gogolook.models import Task, TaskSchema, TaskUpdateSchema
from gogolook.services import TaskCRUDService


@pytest.fixture()
def task_service(mock_db_session, mock_logger):
    task_service = TaskCRUDService(
        model=Task,
        schema=TaskSchema,
        session=mock_db_session,
        logger=mock_logger,
        update_schema=TaskUpdateSchema,
    )

    return task_service


@pytest.fixture()
def dummy_tasks(task_service):
    tasks = [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
    tasks = [task_service.create(obj=task) for task in tasks]

    return tasks


def test_task_service_list(task_service):

    tasks = task_service.list()

    assert len(tasks) == 0


def test_task_service_list_dummy(task_service, dummy_tasks):

    tasks = task_service.list()

    assert len(tasks) == len(dummy_tasks)


@pytest.mark.parametrize(
    "obj", [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
)
def test_task_service_create(task_service, obj):
    task = task_service.create(obj=obj)

    assert task.name == obj["name"]
    assert task.status == 0


def test_task_service_get(task_service, dummy_tasks):
    task = task_service.get(id=dummy_tasks[0].id)

    assert task == dummy_tasks[0]


def test_task_service_update(task_service, dummy_tasks):
    obj = {"name": "updated", "status": 1}
    task = task_service.update(db_obj=dummy_tasks[0], obj=obj)

    assert task.id == dummy_tasks[0].id
    assert task.status == obj["status"]


def test_task_service_delete(task_service, dummy_tasks):
    task_service.delete(dummy_tasks[0])

    task = task_service.get(id=dummy_tasks[0].id)
    assert task is None
