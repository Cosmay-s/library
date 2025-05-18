from fastapi import FastAPI
from library_api.routers import book, borrow, reader, user

app = FastAPI()

# Регистрация роутов
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(book.router, prefix="/books", tags=["books"])
app.include_router(reader.router, prefix="/readers", tags=["readers"])
app.include_router(borrow.router, prefix="/borrow", tags=["borrow"])

# Стартовое сообщение
@app.get("/")
async def root():
    return {"message": "Library API is running!"}