from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from ....models.dog import Dog, DogCreate
from ....services.dog_service import DogService
from ....db.database import get_db

router = APIRouter()
dog_service = DogService()

@router.post("/", response_model=Dog)
async def create_dog(dog: DogCreate, db: Session = Depends(get_db)):
    try:
        return await dog_service.create_dog(db, dog)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[Dog])
async def search_dogs(
    latitude: Optional[float] = Query(None),
    longitude: Optional[float] = Query(None),
    max_distance: Optional[float] = Query(None, gt=0),
    breed: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, gt=0),
    max_price: Optional[float] = Query(None, gt=0),
    db: Session = Depends(get_db)
):
    return await dog_service.search_dogs(
        db,
        latitude=latitude,
        longitude=longitude,
        max_distance=max_distance,
        breed=breed,
        min_price=min_price,
        max_price=max_price
    )