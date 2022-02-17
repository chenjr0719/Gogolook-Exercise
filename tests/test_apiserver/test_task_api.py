import pytest

from gogolook.apiserver.task.task import TaskAPI


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
    assert "result" in resp
    assert isinstance(resp["result"], dict)

    result = resp["result"]
    assert "id" in result
    assert result["id"] == dummy_tasks[0].id
    assert "name" in result
    assert result["name"] == dummy_tasks[0].name
    assert "status" in result
    assert result["status"] == 0


def test_task_api_update(client, dummy_tasks):
    json_body = {"name": "updated", "status": 1}
    resp = client.put(f"/tasks/{dummy_tasks[0].id}", json=json_body)
    assert resp.status_code == 200

    resp = resp.json
    assert "result" in resp
    assert isinstance(resp["result"], dict)

    result = resp["result"]
    assert "id" in result
    assert result["id"] == dummy_tasks[0].id
    assert "name" in result
    assert result["name"] == json_body["name"]
    assert "status" in result
    assert result["status"] == json_body["status"]


def test_task_api_delete(client, dummy_tasks):
    resp = client.delete(f"/tasks/{dummy_tasks[0].id}")
    assert resp.status_code == 200

    resp = resp.json
    assert isinstance(resp, dict)
    assert resp == {}
