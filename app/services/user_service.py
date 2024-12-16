from typing import Optional
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime
from passlib.context import CryptContext

from ..models.user import User, UserCreate
from ..db import models
from ..utils.validators import validate_phone

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self):
        self.pwd_context = pwd_context
        
    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)
    
    async def create_user(self, db: Session, user: UserCreate) -> User:
        if not validate_phone(user.phone):
            raise ValueError("Invalid Kenyan phone number format")
        
        db_user = models.User(
            id=str(uuid4()),
            name=user.name,
            email=user.email,
            phone=user.phone,
            location=user.location.dict(),
            hashed_password=self.get_password_hash(user.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return User(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            phone=db_user.phone,
            location=user.location,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        )
    
    async def get_user(self, db: Session, user_id: str) -> Optional[User]:
        db_user = db.query(models.User).filter(models.User.id == user_id).first()
        if db_user is None:
            return None
            
        return User(
            id=db_user.id,
            name=db_user.name,
            email=db_user.email,
            phone=db_user.phone,
            location=db_user.location,
            created_at=db_user.created_at,
            updated_at=db_user.updated_at
        )