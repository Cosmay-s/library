from sqlalchemy.orm import Session
from library_api.models import BorrowedBook, Book
from datetime import datetime


def borrow_book(db: Session, book_id: int, reader_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book or book.copies_count <= 0:
        return None

    borrowed_count = db.query(BorrowedBook).filter(
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date is None
    ).count()

    if borrowed_count >= 3:
        return None

    borrowed_book = BorrowedBook(book_id=book.id, reader_id=reader_id,
                                 borrow_date=datetime.now())
    db.add(borrowed_book)
    db.commit()
    book.copies_count -= 1
    db.commit()

    return borrowed_book


def return_book(db: Session, book_id: int, reader_id: int):
    borrowed_book = db.query(BorrowedBook).filter(
        BorrowedBook.book_id == book_id,
        BorrowedBook.reader_id == reader_id,
        BorrowedBook.return_date is None
    ).first()

    if borrowed_book:
        borrowed_book.return_date = datetime.now()
        db.commit()

        book = db.query(Book).filter(Book.id == book_id).first()
        if book:
            book.copies_count += 1
            db.commit()

        return borrowed_book
    return None
