from fastapi import HTTPException, UploadFile, status
from fastapi.responses import StreamingResponse

from src.infrastructure.minio import ensure_bucket, get_content_type
from src.infrastructure.minio import get_file as get_file_from_minio
from src.infrastructure.minio import upload_file as upload_file_to_minio


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
    
async def get_file(object_name: str) ->  StreamingResponse:
    try: 
        return StreamingResponse(
            get_file_from_minio(object_name),
            media_type=get_content_type(object_name)
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail={"error": "Failed to get file url from storage"}
        )