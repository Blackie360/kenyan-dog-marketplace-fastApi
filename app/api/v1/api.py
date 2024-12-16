from fastapi import APIRouter
from .endpoints import dogs, users

router = APIRouter()
router.include_router(dogs.router, prefix="/dogs", tags=["dogs"])
router.include_router(users.router, prefix="/users", tags=["users"])