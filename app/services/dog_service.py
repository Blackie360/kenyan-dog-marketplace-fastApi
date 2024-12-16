from typing import List, Optional
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime

from ..models.dog import Dog, DogCreate
from ..db import models
from ..utils.geolocation import is_within_kenya, calculate_distance

class DogService:
    async def create_dog(self, db: Session, dog: DogCreate) -> Dog:
        if not is_within_kenya(dog.location.latitude, dog.location.longitude):
            raise ValueError("Location must be within Kenya")
        
        db_dog = models.Dog(
            id=str(uuid4()),
            name=dog.name,
            breed=dog.breed,
            age_months=dog.age_months,
            price=dog.price,
            description=dog.description,
            location=dog.location.dict(),
            owner_id=dog.owner_id
        )
        db.add(db_dog)
        db.commit()
        db.refresh(db_dog)
        
        return Dog(
            id=db_dog.id,
            name=db_dog.name,
            breed=db_dog.breed,
            age_months=db_dog.age_months,
            price=db_dog.price,
            description=db_dog.description,
            location=dog.location,
            owner_id=db_dog.owner_id,
            created_at=db_dog.created_at,
            updated_at=db_dog.updated_at
        )
    
    async def search_dogs(
        self,
        db: Session,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        max_distance: Optional[float] = None,
        breed: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None
    ) -> List[Dog]:
        query = db.query(models.Dog)
        
        if breed:
            query = query.filter(models.Dog.breed == breed)
        if min_price is not None:
            query = query.filter(models.Dog.price >= min_price)
        if max_price is not None:
            query = query.filter(models.Dog.price <= max_price)
            
        dogs = query.all()
        
        # Filter by distance if coordinates are provided
        if latitude and longitude and max_distance:
            dogs = [
                dog for dog in dogs
                if calculate_distance(
                    (latitude, longitude),
                    (dog.location["latitude"], dog.location["longitude"])
                ) <= max_distance
            ]
            
        return [
            Dog(
                id=dog.id,
                name=dog.name,
                breed=dog.breed,
                age_months=dog.age_months,
                price=dog.price,
                description=dog.description,
                location=dog.location,
                owner_id=dog.owner_id,
                created_at=dog.created_at,
                updated_at=dog.updated_at
            )
            for dog in dogs
        ]