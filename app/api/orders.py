from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.models.users import User
from app.schemas.order import Order, OrderCreate
from app.repositories.order_repository import order_repository
from app.api.deps import get_current_user, get_db

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order_in.user_id = current_user.id
    return order_repository.create(db, order_in)

@router.get("/", response_model=List[Order])
def read_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    orders = order_repository.get_all(db)
    return orders
