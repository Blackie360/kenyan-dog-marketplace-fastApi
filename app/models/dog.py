from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from .location import Location
from ..utils.constants import DOG_BREEDS

class DogBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    breed: str = Field(..., description="Must be a valid dog breed")
    age_months: int = Field(..., ge=1, le=240)
    price: float = Field(..., gt=0)
    description: Optional[str] = Field(None, max_length=1000)
    location: Location
    
    @validator('breed')
    def validate_breed(cls, v):
        if v not in DOG_BREEDS:
            raise ValueError(f"Invalid breed. Must be one of: {', '.join(DOG_BREEDS)}")
        return v

class DogCreate(DogBase):
    owner_id: str

class Dog(DogBase):
    id: str
    owner_id: str
    created_at: datetime
    updated_at: datetime