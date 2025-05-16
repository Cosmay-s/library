from fastapi import APIRouter
from library_api.schemas import Book

router = APIRouter()


@router.post("/create")
async def create_book(book: Book):
    return {f"Book '{book.title}' created successfully"}


@router.get("/")
async def get_books():
    return {"books": []}