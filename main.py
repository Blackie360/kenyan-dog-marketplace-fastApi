from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database, location_utils

# Initialize the FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/dogs/", response_model=schemas.Dog)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)):
    # Get coordinates for the provided location
    latitude, longitude = location_utils.get_coordinates(dog.location)
    
    db_dog = models.Dog(**dog.dict(), latitude=latitude, longitude=longitude)
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

@app.get("/dogs/", response_model=list[schemas.Dog])
def get_dogs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Dog).offset(skip).limit(limit).all()

@app.get("/dogs/{dog_id}", response_model=schemas.Dog)
def get_dog(dog_id: int, db: Session = Depends(get_db)):
    db_dog = db.query(models.Dog).filter(models.Dog.id == dog_id).first()
    if not db_dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog
