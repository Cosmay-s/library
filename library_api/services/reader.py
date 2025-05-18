from sqlalchemy.orm import Session
from library_api.repos.reader import create_reader, get_readers, get_reader_by_id
from library_api.schemas import ReaderCreate


def create_reader_service(db: Session, reader: ReaderCreate):
    return create_reader(db, reader)


def get_readers_service(db: Session, skip: int = 0, limit: int = 10):
    return get_readers(db, skip, limit)


def get_reader_by_id_service(db: Session, reader_id: int):
    return get_reader_by_id(db, reader_id)
