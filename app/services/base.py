from sqlalchemy.sql.expression import Executable
from typing import Any, List


class dbBase:
    def __init__(self, db: List[dict]) -> None:
        self.db = db

class BaseService(dbBase):
    """Base service for all"""
class BaseDataManager(dbBase):
    """Base db manager class"""
    def get_one(self, select_query: Executable) -> Any:
        return self.session.scalar(select_query)
    def add_one(self, model: dict) -> None:
        self.db.append(model)
        return model
    def get_all(self) -> Any:
        return self.db


