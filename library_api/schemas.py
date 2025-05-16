from pydantic import BaseModel, EmailStr
from typing import Optional


# Схема для пользователя
class User(BaseModel):
    email: EmailStr
    password: str

# Схема для книги
class Book(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    copies_count: int

# Схема для читателя
class ReaderCreate(BaseModel):
    name: str
    email: EmailStr

# Схема для выдачи книги
class BorrowBook(BaseModel):
    book_id: int
    reader_id: int
