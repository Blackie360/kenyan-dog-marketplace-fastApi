from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from .location import Location

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(..., description="Kenyan phone number")
    location: Location

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime