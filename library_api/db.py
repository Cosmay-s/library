from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from library_api.models import Base
from contextlib import contextmanager


DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
