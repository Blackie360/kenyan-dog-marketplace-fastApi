from pydantic import BaseModel

class DogBase(BaseModel):
    name: str
    breed: str
    age: int
    price: int
    location: str

class DogCreate(DogBase):
    pass

class Dog(DogBase):
    id: int
    latitude: float | None = None
    longitude: float | None = None

    class Config:
        orm_mode = True
