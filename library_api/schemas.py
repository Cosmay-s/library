from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# --- User Schemas ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str 

    class Config:
        from_attributes = True


class User(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


# --- Book Schemas ---
class BookCreate(BaseModel):
    title: str
    author: str
    year_published: Optional[int] = None
    isbn: Optional[str] = None
    copies_count: int

    class Config:
        from_attributes = True


class Book(BookCreate):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# --- Reader Schemas ---
class ReaderCreate(BaseModel):
    name: str
    email: EmailStr

    class Config:
        from_attributes = True


class ReaderResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# --- Borrowing Schemas ---
class BorrowBook(BaseModel):
    book_id: int
    reader_id: int


class BorrowedBookResponse(BaseModel):
    id: int
    book_id: int
    reader_id: int
    borrowed_at: datetime
    returned_at: Optional[datetime] = None

    class Config:
        from_attributes = True
