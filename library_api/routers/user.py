from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from library_api.schemas import User
from library_api.services import user as user_service
from library_api.db import get_db

router = APIRouter()


@router.post("/register")
def register_user(user: User, db: Session = Depends(get_db)):
    try:
        user_service.register_user(db, user)
        return {"message": f"User {user.email} registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login")
def login_user(user: User, db: Session = Depends(get_db)):
    token = user_service.authenticate_user(db, user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
