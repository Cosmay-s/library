from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class UserRegister(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/register")
async def register_user(user: UserRegister):
    return {f"User {user.email} registered successfully"}


async def login_user(user: UserLogin):
    return {"token_type": "bearer"}