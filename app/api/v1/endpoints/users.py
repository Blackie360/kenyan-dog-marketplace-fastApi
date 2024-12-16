from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ....models.user import User, UserCreate
from ....services.user_service import UserService
from ....db.database import get_db

router = APIRouter()
user_service = UserService()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return await user_service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    user = await user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user