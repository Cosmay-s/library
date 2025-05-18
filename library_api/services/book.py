from sqlalchemy.orm import Session
from library_api.repos.book import create_book, get_books, get_book_by_id, update_book, delete_book
from library_api.schemas import BookCreate


def create_book_service(db: Session, book: BookCreate):
    return create_book(db, book)


def get_books_service(db: Session, skip: int = 0, limit: int = 10):
    return get_books(db, skip, limit)


def get_book_by_id_service(db: Session, book_id: int):
    return get_book_by_id(db, book_id)


def update_book_service(db: Session, book_id: int, updated_book: BookCreate):
    return update_book(db, book_id, updated_book)


def delete_book_service(db: Session, book_id: int):
    return delete_book(db, book_id)
