from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.schemas.user import UserCreate, User, TokenData, TokenRefresh, Token
from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token, create_refresh_token
from app.api.deps import get_db
from app.core.config import settings

router = APIRouter()

@router.post("/auth/register", response_model=User)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = UserRepository.create_user(db, user_in)
    return user

@router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserRepository().authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"user_id": user.id})
    refresh_token = create_refresh_token(data={"user_id": user.id})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

@router.post("/auth/refresh", response_model=Token)
def refresh_token(token_refresh: TokenRefresh, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token_refresh.refresh_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        token_data = TokenData(user_id=str(user_id))
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    user = UserRepository().get(db=db, id=user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    access_token = create_access_token(data={"user_id": user.id})
    return {"access_token": access_token}
