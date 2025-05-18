from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


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
