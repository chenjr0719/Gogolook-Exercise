import pytest


def test_task_service_list(mock_task_service):

    tasks = mock_task_service.list()

    assert len(tasks) == 0


def test_task_service_list_dummy(mock_task_service, dummy_tasks):

    tasks = mock_task_service.list()

    assert len(tasks) == len(dummy_tasks)


@pytest.mark.parametrize(
    "obj", [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
)
def test_task_service_create(mock_task_service, obj):
    task = mock_task_service.create(obj=obj)

    assert task.name == obj["name"]
    assert task.status == 0


def test_task_service_get(mock_task_service, dummy_tasks):
    task = mock_task_service.get(id=dummy_tasks[0].id)

    assert task == dummy_tasks[0]


def test_task_service_update(mock_task_service, dummy_tasks):
    obj = {"name": "updated", "status": 1}
    task = mock_task_service.update(db_obj=dummy_tasks[0], obj=obj)

    assert task.id == dummy_tasks[0].id
    assert task.status == obj["status"]


def test_task_service_delete(mock_task_service, dummy_tasks):
    mock_task_service.delete(dummy_tasks[0])

    task = mock_task_service.get(id=dummy_tasks[0].id)
    assert task is None
