from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from library_api.schemas import BookCreate
from library_api.services.book import create_book_service, get_books_service, get_book_by_id_service, update_book_service, delete_book_service
from library_api.db import get_db


router = APIRouter()


@router.post("/create")
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = create_book_service(db, book)
    return {"message": f"Book '{db_book.title}' created successfully", "book": db_book}


@router.get("/")
async def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = get_books_service(db, skip, limit)
    return {"books": books}


@router.get("/{book_id}")
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = get_book_by_id_service(db, book_id)
    if book:
        return {"book": book}
    raise HTTPException(status_code=404, detail="Книга не найдена.")


@router.put("/{book_id}")
async def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    book = update_book_service(db, book_id, updated_book)
    if book:
        return {"message": f"Book '{book.title}' updated successfully", "book": book}
    return {"message": "Book not found"}, 404


@router.delete("/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = delete_book_service(db, book_id)
    if book:
        return {"Удалена книга": book}
    raise HTTPException(status_code=404, detail="Книга не найдена.")
