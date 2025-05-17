from datetime import datetime, UTC
from typing import Optional, List
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, UniqueConstraint


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True,
                                       nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC),
                                                 onupdate=datetime.now(tz=UTC))


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    year_published: Mapped[Optional[int]]
    isbn: Mapped[Optional[str]] = mapped_column(String, unique=True)
    copies_count: Mapped[int] = mapped_column(default=1, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(default=None)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC),
                                                 onupdate=datetime.now(tz=UTC))
    borrowed_books: Mapped[List["BorrowedBook"]] = relationship(
                                                    back_populates="book")


class Reader(Base):
    __tablename__ = "readers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC),
                                                 onupdate=datetime.now(tz=UTC))
    borrowed_books: Mapped[List["BorrowedBook"]] = relationship(
                                                    back_populates="reader")


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"),
                                         nullable=False)
    reader_id: Mapped[int] = mapped_column(ForeignKey("readers.id"),
                                           nullable=False)
    borrow_date: Mapped[datetime] = mapped_column(default=datetime.now(tz=UTC))
    return_date: Mapped[Optional[datetime]]
    book: Mapped["Book"] = relationship(back_populates="borrowed_books")
    reader: Mapped["Reader"] = relationship(back_populates="borrowed_books")

    __table_args__ = (
        UniqueConstraint("book_id", "reader_id", "return_date",
                         name="uq_borrow_unique_active"),
    )
