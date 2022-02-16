import pytest

from gogolook.apiserver.task.task import TaskAPI
from gogolook.services.task import get_task_service


@pytest.fixture()
def mock_task_service(mock_db_session, mock_logger):

    task_service = get_task_service(session=mock_db_session, logger=mock_logger)
    return task_service


@pytest.fixture()
def dummy_tasks(mock_task_service):
    tasks = [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
    tasks = [mock_task_service.create(obj=task) for task in tasks]

    return tasks


@pytest.fixture(autouse=True)
def mock_task_api(app, mock_task_service, mock_logger):
    task_api = TaskAPI(task_service=mock_task_service, logger=mock_logger)
    app.register_blueprint(task_api, url_prefix="/tasks")


def test_task_api_list(client):
    resp = client.get("/tasks/")
    assert resp.status_code == 200

    resp = resp.json
    assert "result" in resp
    assert isinstance(resp["result"], list)
    assert len(resp["result"]) == 0


def test_task_api_list_dummy(client, dummy_tasks):

    resp = client.get("/tasks/")
    assert resp.status_code == 200

    resp = resp.json
    assert "result" in resp
    assert isinstance(resp["result"], list)
    assert len(resp["result"]) == len(dummy_tasks)


@pytest.mark.parametrize(
    "json_body", [{"name": "sleep"}, {"name": "eat"}, {"name": "買晚餐"}, {"name": "買早餐"}]
)
def test_task_api_create(client, json_body):
    resp = client.post("/tasks/", json=json_body)

    assert resp.status_code == 201

    resp = resp.json
    assert "result" in resp
    assert isinstance(resp["result"], dict)

    result = resp["result"]
    assert result["name"] == json_body["name"]
    assert result["status"] == 0


def test_task_api_get(client, dummy_tasks):
    resp = client.get(f"/tasks/{dummy_tasks[0].id}")
    assert resp.status_code == 200

    resp = resp.json
    assert isinstance(resp, dict)
    assert "id" in resp
    assert resp["id"] == dummy_tasks[0].id
    assert "name" in resp
    assert resp["name"] == dummy_tasks[0].name
    assert "status" in resp
    assert resp["status"] == 0


def test_task_api_update(client, dummy_tasks):
    json_body = {"name": "updated", "status": 1}
    resp = client.put(f"/tasks/{dummy_tasks[0].id}", json=json_body)
    assert resp.status_code == 200

    resp = resp.json
    assert isinstance(resp, dict)
    assert "id" in resp
    assert resp["id"] == dummy_tasks[0].id
    assert "name" in resp
    assert resp["name"] == json_body["name"]
    assert "status" in resp
    assert resp["status"] == json_body["status"]


def test_task_api_delete(client, dummy_tasks):
    resp = client.delete(f"/tasks/{dummy_tasks[0].id}")
    assert resp.status_code == 200

    resp = resp.json
    assert isinstance(resp, dict)
    assert resp == {}
