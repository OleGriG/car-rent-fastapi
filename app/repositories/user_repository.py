import os

from sqlalchemy.orm import Session
import bcrypt

from app.db.models.users import User
from app.repositories.base import Repository
from app.schemas.user import UserCreate
from app.core.utils import hash_password
from app.core.config import settings

class UserRepository(Repository):
    @staticmethod
    def create_user(db: Session, user_create: UserCreate):
        hashed_password = hash_password(user_create.password)
        db_user = User(email=user_create.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate(db: Session, email: str, password: str) -> User:
        user = db.query(User).filter(User.email==email).first()
        if not user:
            return None
        if not user.hashed_password == hash_password(password):
            return None
        return user
