from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String, index=True)
    age = Column(Integer)
    price = Column(Integer)
    location = Column(String, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
