from datetime import timedelta
import os
from fastapi import UploadFile
from .bucket import BUCKET_NAME
from .client import minio_client


async def upload_file(file: UploadFile) -> str:
     # Generate unique file name
    file_extension = os.path.splitext(file.filename)[1]
    object_name = f"{os.urandom(16).hex()}{file_extension}"
    file_content = await file.read()
        
    minio_client.put_object(
        bucket_name=BUCKET_NAME,
        object_name=object_name,
        data=file_content,
        length=len(file_content),
        content_type=file.content_type
    )

    return object_name
        
def get_file_url(object_name: str) -> str:
    return minio_client.presigned_get_object(
        bucket_name=BUCKET_NAME,
        object_name=object_name,
        expires=timedelta(minutes=1)
    )