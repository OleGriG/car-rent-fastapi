from pydantic import BaseModel
from app.schemas.user import User
from app.schemas.car import Car

class OrderBase(BaseModel):
    user_id: int
    car_id: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    user: User
    car: Car

    class Config:
        orm_mode = True
