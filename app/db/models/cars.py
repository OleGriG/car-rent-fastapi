import os

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_media import StoreManager, File, FileSystemStore

# Настройка хранилища файлов
store_directory = os.path.expanduser('~/Dev/car-rent-fastapi')
store = FileSystemStore(store_directory, '/')
StoreManager.register('fs', store)
from app.db.session import Base

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer)
    orders = relationship("Order", back_populates="car")
