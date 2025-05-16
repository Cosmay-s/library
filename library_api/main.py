from fastapi import FastAPI
from library_api.routers import auth, book, borrow, reader

app = FastAPI()

# Регистрация роутов
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(book.router, prefix="/books", tags=["books"])
app.include_router(reader.router, prefix="/readers", tags=["readers"])
app.include_router(borrow.router, prefix="/borrow", tags=["borrow"])