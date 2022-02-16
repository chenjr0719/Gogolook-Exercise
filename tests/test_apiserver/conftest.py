import pytest
from flask import Flask

from gogolook.apiserver.app import register_error_handlers


@pytest.fixture()
def app():
    app = Flask(__name__)

    register_error_handlers(app)

    app.config.update({"TESTING": True})

    return app


@pytest.fixture()
def client(app):
    return app.test_client()
