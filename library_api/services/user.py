from sqlalchemy.orm import Session
from library_api.schemas import UserCreate
from library_api.repos import user as user_repo


# Регистрация пользователя
def register_user(db: Session, user_data: UserCreate):
    existing_user = user_repo.get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Пользователь с таким email уже зарегистрирован")
    return user_repo.create_user(db, user_data)


# Аутентификация пользователя
def authenticate_user(db: Session, email: str, password: str):
    db_user = user_repo.get_user_by_email(db, email)
    if not db_user or db_user.password != password:  # Сравниваем пароли в открытом виде
        return None

    return "fake-token"  # Возвращаем фиктивный токен для демонстрации
