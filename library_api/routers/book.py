from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from library_api.schemas import BookCreate, Book
from library_api.services.book import (
    create_book_service,
    get_books_service,
    get_book_by_id_service,
    update_book_service,
    delete_book_service,
)
from library_api.db import get_db

router = APIRouter()


# Создание книги
@router.post("/create", response_model=Book, summary="Создание книги", description="Этот маршрут позволяет создать новую книгу в базе данных.")
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Создает книгу в базе данных с использованием переданных данных.
    - **book**: Объект с данными для создания книги.
    """
    db_book = create_book_service(db, book)
    return {"message": f"Книга '{db_book.title}' успешно создана", "book": db_book}


# Получение списка книг
@router.get("/", response_model=list[Book], summary="Получение списка книг", description="Этот маршрут позволяет получить список книг с возможностью пагинации.")
async def get_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Возвращает список книг с возможностью указать параметры для пагинации.
    - **skip**: Количество пропущенных книг (по умолчанию 0).
    - **limit**: Максимальное количество книг, которое будет возвращено (по умолчанию 10).
    """
    books = get_books_service(db, skip, limit)
    return {"books": books}


# Получение книги по ID
@router.get("/{book_id}", response_model=Book, summary="Получение книги по ID", description="Этот маршрут позволяет получить информацию о книге по ее ID.")
async def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    """
    Возвращает книгу по её ID.
    - **book_id**: Уникальный идентификатор книги.
    """
    book = get_book_by_id_service(db, book_id)
    if book:
        return {"book": book}
    raise HTTPException(status_code=404, detail="Книга не найдена")


# Обновление книги
@router.put("/{book_id}", response_model=Book, summary="Обновление книги", description="Этот маршрут позволяет обновить информацию о книге по ее ID.")
async def update_book(book_id: int, updated_book: BookCreate, db: Session = Depends(get_db)):
    """
    Обновляет информацию о книге.
    - **book_id**: Уникальный идентификатор книги.
    - **updated_book**: Объект с обновленными данными книги.
    """
    book = update_book_service(db, book_id, updated_book)
    if book:
        return {"message": f"Книга '{book.title}' успешно обновлена", "book": book}
    raise HTTPException(status_code=404, detail="Книга не найдена")


# Удаление книги
@router.delete("/{book_id}", summary="Удаление книги", description="Этот маршрут позволяет удалить книгу по её ID.")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Удаляет книгу по её ID.
    - **book_id**: Уникальный идентификатор книги.
    """
    book = delete_book_service(db, book_id)
    if book:
        return {"message": f"Книга '{book.title}' удалена"}
    raise HTTPException(status_code=404, detail="Книга не найдена")
