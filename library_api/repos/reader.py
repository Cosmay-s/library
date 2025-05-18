from sqlalchemy.orm import Session
from library_api.models import Reader
from library_api.schemas import ReaderCreate


def create_reader(db: Session, reader: ReaderCreate):
    db_reader = Reader(name=reader.name, email=reader.email)
    db.add(db_reader)
    db.commit()
    db.refresh(db_reader)
    return db_reader


def get_readers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reader).offset(skip).limit(limit).all()


def get_reader_by_id(db: Session, reader_id: int):
    return db.query(Reader).filter(Reader.id == reader_id).first()
