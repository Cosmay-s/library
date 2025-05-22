from pydantic import BaseModel, EmailStr
from typing import Optional


# Схема для регистрации пользователя
class UserCreate(BaseModel):
    email: EmailStr
    password: str  # Пароль в открытом виде, который будет передан от клиента

    class Config:
        orm_mode = True

# Схема для данных пользователя (после создания)
class User(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class Book(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    copies_count: int


class BookCreate(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    copies_count: int


class ReaderCreate(BaseModel):
    name: str
    email: EmailStr


class BorrowBook(BaseModel):
    book_id: int
    reader_id: int
