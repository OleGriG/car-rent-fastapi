from typing import Any, List
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import as_declarative, declared_attr

class Repository:
    def __init__(self, model: Any):
        self.model = model

    def get(self, db: Session, id: Any) -> Any:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[Any]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: Any) -> Any:
        actual_db_item = self.model(**obj_in.dict())
        db.add(actual_db_item)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def remove(self, db: Session, id: Any) -> Any:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
