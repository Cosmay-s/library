from fastapi import APIRouter
from library_api.schemas import User

router = APIRouter()


@router.post("/register")
async def register_user(user: User):
    return {f"User {user.email} registered successfully"}


@router.post("/login")
async def login_user(user: User):
    return {"token_type": "bearer"}
