from flask import Blueprint
from sqlalchemy.orm.session import Session

from gogolook.config import Settings
from gogolook.models import Task
from gogolook.services import TaskCRUDService


class TaskAPI(Blueprint):
    def __init__(
        self,
        settings: Settings,
        session: Session,
        name="TaskAPI",
        import_name=__name__,
        static_folder=None,
        static_url_path=None,
        template_folder=None,
        url_prefix=None,
        subdomain=None,
        url_defaults=None,
        root_path=None,
        cli_group=...,
    ):
        super().__init__(
            name,
            import_name,
            static_folder,
            static_url_path,
            template_folder,
            url_prefix,
            subdomain,
            url_defaults,
            root_path,
            cli_group,
        )

        self.task_service = TaskCRUDService(model=Task, session=session)
        self.add_url_rule("/", "list", self.list, methods=["GET"])
        self.add_url_rule("/", "create", self.create, methods=["POST"])
        self.add_url_rule("/<id>", "get", self.get, methods=["GET"])
        self.add_url_rule("/<id>", "update", self.update, methods=["PUT"])
        self.add_url_rule("/<id>", "delete", self.delete, methods=["DELETE"])

    def list(self):
        pass

    def create(self):
        pass

    def get(self, id: int):
        pass

    def update(self, id: int):
        pass

    def delete(self, id: int):
        pass
