from turtle import rt
from flask import Flask
from gogolook.config import Settings
from gogolook.db import get_session
from gogolook.apiserver.task import TaskAPI


def get_app():

    settings = Settings()
    db_session = get_session(settings)

    app = Flask(__name__)

    task_api = TaskAPI(settings=settings, session=db_session)
    app.register_blueprint(task_api, url_prefix="/task")

    return app
