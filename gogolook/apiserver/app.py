from flask import Flask, jsonify

from gogolook.apiserver.errors import BadRequest, NotFound, UnknownError
from gogolook.apiserver.task import TaskAPI
from gogolook.config import Settings
from gogolook.db import get_session
from gogolook.logger import get_logger
from gogolook.models import Base
from gogolook.services import get_task_service


def get_app():  # noqa

    settings = Settings()
    db_session = get_session(settings)
    logger = get_logger(settings=settings)

    Base.metadata.create_all(bind=db_session.get_bind())

    app = Flask(__name__)

    task_service = get_task_service(session=db_session, logger=logger)
    task_api = TaskAPI(task_service=task_service, logger=logger)
    app.register_blueprint(task_api, url_prefix="/tasks")

    register_error_handlers(app)

    return app


def register_error_handlers(app):
    def err_resp(e):
        return jsonify(e.to_dict()), e.status_code

    app.register_error_handler(UnknownError, err_resp)
    app.register_error_handler(BadRequest, err_resp)
    app.register_error_handler(NotFound, err_resp)


app = get_app()  # noqa
