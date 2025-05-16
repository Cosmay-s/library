from fastapi import APIRouter
from library_api.schemas import ReaderCreate

router = APIRouter()


@router.post("/create")
async def create_reader(reader: ReaderCreate):
    return {f"Reader '{reader.name}' created successfully"}


@router.get("/")
async def get_readers():
    return {"readers": []} 