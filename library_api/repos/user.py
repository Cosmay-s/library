from sqlalchemy.orm import Session
from library_api.models import User
from library_api.schemas import UserCreate
from fastapi import HTTPException


# Создание пользователя
def create_user(db: Session, user: UserCreate):
    # Проверяем, существует ли пользователь с таким email
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400,
                            detail="Пользователь с таким email уже существует")

    # Создаем нового пользователя
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()  # Подтверждаем изменения
    db.refresh(db_user)  # Обновляем объект, чтобы получить id пользователя
    return db_user


# Получить пользователя по email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# Логин пользователя
def login_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first() 
    if db_user and db_user.password == user.password:
        return {"message": "Успешный вход"}
    else:
        raise HTTPException(status_code=401, detail="Неверные учетные данные")
