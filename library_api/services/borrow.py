from sqlalchemy.orm import Session
from library_api.repos.borrow import borrow_book, return_book


def borrow_book_service(db: Session, book_id: int, reader_id: int):
    return borrow_book(db, book_id, reader_id)


def return_book_service(db: Session, book_id: int, reader_id: int):
    return return_book(db, book_id, reader_id)
