from fastapi import APIRouter
from library_api.schemas import BorrowBook

router = APIRouter()


@router.post("/borrow")
async def borrow_book(borrow: BorrowBook):
    return {"message": f"Book {borrow.book_id} borrowed by reader {borrow.reader_id}"}


@router.post("/return")
async def return_borrowed_book(borrow: BorrowBook):
    return {"message": f"Book {borrow.book_id} returned by reader {borrow.reader_id}"}