from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from library_api.schemas import UserCreate
from library_api.services import user as user_service
from library_api.db import get_db

router = APIRouter()


@router.post("/register", summary="Регистрация пользователя",
             description="Этот маршрут позволяет зарегистрировать нового пользователя.")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_service.register_user(db, user)
        return {"message": f"Пользователь {user.email} успешно зарегистрирован"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", summary="Авторизация пользователя",
             description="Этот маршрут позволяет пользователю войти в систему.")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    token = user_service.authenticate_user(db, user.email, user.password)
    if token:
        return {"message": "Успешный вход", "token": token}
    raise HTTPException(status_code=401, detail="Неверные учетные данные")
