from sqlalchemy.orm import Session
from library_api.models import Book
from library_api.schemas import BookCreate


def create_book(db: Session, book: BookCreate):
    db_book = Book(
        title=book.title,
        author=book.author,
        year_published=book.year_published,
        isbn=book.isbn,
        copies_count=book.copies_count
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, updated_book: BookCreate):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db_book.title = updated_book.title
        db_book.author = updated_book.author
        db_book.year_published = updated_book.year_published
        db_book.isbn = updated_book.isbn
        db_book.copies_count = updated_book.copies_count
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
