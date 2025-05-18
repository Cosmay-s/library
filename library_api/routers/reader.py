from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from library_api.schemas import ReaderCreate
from library_api.services.reader import create_reader_service, get_readers_service, get_reader_by_id_service
from library_api.db import get_db


router = APIRouter()


@router.post("/create")
async def create_reader(reader: ReaderCreate, db: Session = Depends(get_db)):
    created_reader = create_reader_service(db, reader)
    return {"message": f"Reader '{created_reader.name}' created successfully", "reader": created_reader}


@router.get("/")
async def get_readers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    readers = get_readers_service(db, skip, limit)
    return {"readers": readers}


@router.get("/{reader_id}")
async def get_reader_by_id(reader_id: int, db: Session = Depends(get_db)):
    reader = get_reader_by_id_service(db, reader_id)
    if reader:
        return {"reader": reader}
    return {"message": "Reader not found"}, 404
