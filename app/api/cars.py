from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.car import Car, CarCreate
from app.repositories.car_repository import car_repository
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=Car)
def create_car(car_in: CarCreate, db: Session = Depends(get_db)):
    return car_repository.create(db, car_in)

@router.get("/", response_model=List[Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cars = car_repository.get_all(db)
    return cars
