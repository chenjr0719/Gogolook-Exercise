from gogolook.models import Base
from sqlalchemy import Column, String, Enum
from enum import IntEnum


class TaskStatus(IntEnum):
    created = 0
    completed = 1
    canceled = 2


class Task(Base):
    name = Column(String)
    status = Column(Enum(TaskStatus))
