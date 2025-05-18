from sqlalchemy.orm import Session
from library_api.schemas import UserCreate
from library_api.repos import user as user_repo
from library_api.auth.password import verify_password
from library_api.auth.jwt import create_access_token


def register_user(db: Session, user_data: UserCreate):
    existing_user = user_repo.get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Email already registered")
    return user_repo.create_user(db, user_data)


def authenticate_user(db: Session, email: str, password: str):
    db_user = user_repo.get_user_by_email(db, email)
    if not db_user or not verify_password(password, db_user.password_hash):
        return None
    token = create_access_token({"sub": db_user.email})
    return token
