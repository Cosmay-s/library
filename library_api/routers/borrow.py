from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from library_api.schemas import BorrowBook
from library_api.services.borrow import borrow_book_service, return_book_service
from library_api.db import get_db


router = APIRouter()


@router.post("/borrow")
async def borrow_book(borrow: BorrowBook, db: Session = Depends(get_db)):
    borrowed_book = borrow_book_service(db, borrow.book_id, borrow.reader_id)
    if borrowed_book:
        return {"message": f"Book {borrow.book_id} borrowed by reader {borrow.reader_id}", "borrowed_book": borrowed_book}
    return {"message": "Could not borrow book"}, 400


@router.post("/return")
async def return_borrowed_book(borrow: BorrowBook, db: Session = Depends(get_db)):
    returned_book = return_book_service(db, borrow.book_id, borrow.reader_id)
    if returned_book:
        return {"message": f"Book {borrow.book_id} returned by reader {borrow.reader_id}", "returned_book": returned_book}
    return {"message": "Could not return book"}, 400
