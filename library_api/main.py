from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from library_api.routers import book, borrow, reader, user
from library_api.db import init_db

app = FastAPI(
    title="Library API",
    description="RESTful API для управления библиотекой",
    version="1.0.0",
)


init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(book.router, prefix="/books", tags=["books"])
app.include_router(reader.router, prefix="/readers", tags=["readers"])
app.include_router(borrow.router, prefix="/borrow", tags=["borrow"])


@app.get("/")
async def root():
    return {"message": "Library API is running!"}
