from fastapi import APIRouter, UploadFile

from src.domain.services import file as service
from src.infrastructure.helpers import CurrentUser


router = APIRouter(
    prefix="/file",
    tags=["file"],
)

@router.post('/upload')
async def upload(user: CurrentUser, file: UploadFile):
    return await service.upload_file(file)

@router.get('/{filename}')
async def get_file(user: CurrentUser, filename: str):
    return await service.get_file(filename)
