from typing import List, TypeVar
from gogolook.models import Base
from sqlalchemy.orm.session import Session
from gogolook.config import Settings

ModelType = TypeVar("ModelType", bound=Base)


class CRUDService:
    def __init__(self, model: ModelType, session: Session) -> None:
        self.model = model
        self.session = session

    def list(self) -> List[ModelType]:
        pass

    def create(self, obj: dict) -> ModelType:
        pass

    def get(self, id: int) -> ModelType:
        pass

    def update(self, id: int, obj: dict) -> ModelType:
        pass

    def delete(self, id: int) -> None:
        pass
