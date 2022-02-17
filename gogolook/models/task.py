from enum import IntEnum
from typing import Optional

from pydantic import Field
from sqlalchemy import Column, Enum, String

from gogolook.models import Base, BaseSchema


class TaskStatus(IntEnum):
    Incomplete = 0
    Complete = 1


class Task(Base):
    name = Column(String(length=100))
    status = Column(Enum(TaskStatus), default=TaskStatus.Incomplete)


class TaskSchema(BaseSchema):
    id: int = Field(description="The id of Task")
    name: str = Field(description="The name of Task")
    status: TaskStatus = Field(
        description="The status of Task", default=TaskStatus.Incomplete
    )


class TaskUpdateSchema(TaskSchema):
    name: Optional[str] = Field(description="The name of Task")
    status: Optional[TaskStatus] = Field(description="The status of Task")
