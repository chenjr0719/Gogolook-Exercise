from logging import Logger

from flask import Blueprint, request

from gogolook.apiserver.errors import BadRequest, NotFound, UnknownError
from gogolook.services import TaskCRUDService


class TaskAPI(Blueprint):
    def __init__(
        self,
        task_service: TaskCRUDService,
        logger: Logger,
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

        self.task_service = task_service
        self.logger = logger

        self.add_url_rule("/", "list", self.list, methods=["GET"])
        self.add_url_rule("/", "create", self.create, methods=["POST"])
        self.add_url_rule("/<id>", "get", self.get, methods=["GET"])
        self.add_url_rule("/<id>", "update", self.update, methods=["PUT"])
        self.add_url_rule("/<id>", "delete", self.delete, methods=["DELETE"])

    def list(self):
        offset = request.args.get("offset", default=0, type=int)
        limit = request.args.get("limit", default=100, type=int)

        try:
            db_objs = self.task_service.list(offset=offset, limit=limit)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        db_objs = [self.task_service.to_dict(db_obj=db_obj) for db_obj in db_objs]

        return {"result": db_objs}

    def create(self):
        try:
            obj = request.get_json()

        except Exception as e:
            self.logger.exception(e)
            raise BadRequest()

        if obj is None:
            raise BadRequest()

        try:
            db_obj = self.task_service.create(obj=obj)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        return {"result": self.task_service.to_dict(db_obj)}, 201

    def get(self, id: int):

        db_obj = self.task_service.get(id=id)
        if db_obj is None:
            raise NotFound()

        return self.task_service.to_dict(db_obj)

    def update(self, id: int):

        try:
            obj = request.get_json()

        except Exception as e:
            self.logger.exception(e)
            raise BadRequest()

        if obj is None:
            raise BadRequest()

        try:
            db_obj = self.task_service.get(id=id)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        if db_obj is None:
            raise NotFound()

        try:
            db_obj = self.task_service.update(db_obj=db_obj, obj=obj)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        return self.task_service.to_dict(db_obj)

    def delete(self, id: int):

        try:
            db_obj = self.task_service.get(id=id)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        if db_obj is None:
            raise NotFound()

        try:
            self.task_service.delete(db_obj)
        except Exception as e:
            self.logger.exception(e)
            raise UnknownError()

        return {}
