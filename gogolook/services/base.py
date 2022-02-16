from logging import Logger
from typing import List, Optional, TypeVar

from sqlalchemy.orm.session import Session

from gogolook.models import Base, BaseSchema, schema_factory

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseSchema)


class CRUDService:
    def __init__(
        self,
        model: ModelType,
        schema: SchemaType,
        session: Session,
        logger: Logger,
        create_schema: Optional[SchemaType] = None,
        update_schema: Optional[SchemaType] = None,
    ) -> None:
        self.model = model
        self.schema = schema_factory(schema, name=f"{self.model.__name__}", excludes=[])
        self.session = session
        self.logger = logger
        self.create_schema = schema_factory(
            create_schema or schema, name=f"{self.model.__name__}Create"
        )
        self.update_schema = schema_factory(
            update_schema or schema, name=f"{self.model.__name__}Update"
        )

    def save(self, db_obj: ModelType) -> ModelType:

        message = f"Saving {self.model.__name__}"
        self.logger.debug(message)

        try:
            self.session.add(db_obj)
            self.session.commit()

        except Exception:
            self.session.rollback()

            message = f"Save {self.model.__name__} failed"
            self.logger.exception(message)
            raise

        self.session.refresh(db_obj)

        message = f"Save {self.model.__name__} succeeded"
        self.logger.debug(message)

        return db_obj

    def list(self, offset: int = 0, limit: int = 100) -> List[ModelType]:

        message = f"Listing {self.model.__name__}"
        self.logger.debug(message)

        try:
            query = self.session.query(self.model)
            db_objs = query.offset(offset=offset).limit(limit=limit).all()

        except Exception:
            self.session.rollback()

            message = f"List {self.model.__name__} failed"
            self.logger.exception(message)
            raise

        message = f"List {self.model.__name__} succeeded"
        self.logger.debug(message)

        return db_objs

    def create(self, obj: dict) -> ModelType:

        message = f"Creating {self.model.__name__}"
        self.logger.debug(message)

        db_obj = self.model()
        try:
            # Convert to schema type to valid input
            if isinstance(obj, dict):
                obj = self.create_schema.parse_obj(obj)

            input_data = obj.dict(exclude_unset=True, exclude_defaults=True)
            for key, value in input_data.items():
                setattr(db_obj, key, value)

            db_obj = self.save(db_obj=db_obj)

        except Exception:
            self.session.rollback()

            message = f"Create {self.model.__name__} failed"
            self.logger.exception(message)
            raise

        message = f"Create {self.model.__name__} succeeded"
        self.logger.debug(message)

        return db_obj

    def get(self, id: int) -> ModelType:

        message = f"Getting {self.model.__name__} {id}"
        self.logger.debug(message)

        try:
            db_obj = self.session.query(self.model).filter(self.model.id == id).first()
        except Exception:
            self.session.rollback()

            message = f"Get {self.model.__name__} {id} failed"
            self.logger.exception(message)
            raise

        message = f"Get {self.model.__name__} {id} succeeded"
        self.logger.debug(message)

        return db_obj

    def update(self, db_obj: ModelType, obj: dict) -> ModelType:

        message = f"Updating {self.model.__name__} {db_obj.id}"
        self.logger.debug(message)

        try:
            # Convert to schema type to valid input
            if isinstance(obj, dict):
                obj = self.update_schema.parse_obj(obj)

            input_data = obj.dict(exclude_unset=True, exclude_defaults=True)
            for key, value in input_data.items():
                setattr(db_obj, key, value)

            db_obj = self.save(db_obj=db_obj)

        except Exception:
            self.session.rollback()

            message = f"Update {self.model.__name__} {db_obj.id} failed"
            self.logger.exception(message)
            raise

        return db_obj

    def delete(self, db_obj: ModelType) -> None:

        message = f"Deleting {self.model.__name__} {db_obj.id}"
        self.logger.debug(message)

        try:
            self.session.delete(db_obj)
            self.session.commit()
        except Exception:
            self.session.rollback()

            message = f"Delete {self.model.__name__} {db_obj.id} failed"
            self.logger.exception(message)
            raise

        return

    def to_dict(self, db_obj: ModelType) -> SchemaType:
        obj = self.schema.from_orm(db_obj)
        obj_dict = obj.dict(exclude={"created_at", "updated_at"})
        return obj_dict
