from datetime import datetime
from typing import List, Type

from pydantic import BaseModel, Field, create_model
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.id}>"


def schema_factory(
    schema_cls: Type[BaseModel],
    name: str = "",
    excludes: List[str] = ["id", "created_at", "updated_at"],
) -> Type[BaseModel]:
    """
    Is used to create a CreateSchema which does not contain pk
    From: https://github.com/awtkns/fastapi-crudrouter/blob/master/fastapi_crudrouter/core/_utils.py#L18
    """
    schema = create_model(__model_name=name or schema_cls.__name__, __base__=schema_cls)
    for exclude in excludes:
        schema.__fields__.pop(exclude, None)
    return schema


class BaseSchema(BaseModel):
    id: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    class Config:
        orm_mode = True
