from typing_extensions import Annotated
from fastapi import File, HTTPException, UploadFile, status
from aiohttp import ClientSession

from src.infrastructure.minio import (
    upload_file as upload_file_to_minio, 
    get_file_url as get_file_url_from_minio,
    ensure_bucket
)


async def upload_file(file: UploadFile) -> str:
    """
    Upload a file to MinIO storage
    Returns the file URL
    """
    try:
        await ensure_bucket()
        return await upload_file_to_minio(file)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail={"error": "Failed to upload file to storage"}
        )
    
async def get_file(object_name: str) ->  Annotated[bytes, File()]:
    try: 
        file_url = get_file_url_from_minio(object_name)
        response = await ClientSession().get(file_url)
        return response.content
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail={"error": "Failed to get file url from storage"}
        )