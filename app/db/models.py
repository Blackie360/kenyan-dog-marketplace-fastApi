from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    hashed_password = Column(String)
    location = Column(JSON)  # Stores Location model as JSON
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    dogs = relationship("Dog", back_populates="owner")

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String, index=True)
    age_months = Column(Integer)
    price = Column(Float)
    description = Column(String, nullable=True)
    location = Column(JSON)  # Stores Location model as JSON
    owner_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    owner = relationship("User", back_populates="dogs")