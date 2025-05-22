import os
from fastapi import UploadFile
from .bucket import BUCKET_NAME
from .client import minio_client


async def upload_file(file: UploadFile) -> str:
    object_name = f"{os.urandom(16).hex()}"
    file_content = file.file
    file_content.seek(0, os.SEEK_END)
    file_size = file_content.tell()
    file_content.seek(0)

        
    minio_client.put_object(
        bucket_name=BUCKET_NAME,
        object_name=object_name,
        data=file_content,
        length=file_size,
        content_type=file.content_type
    )

    return object_name

def get_content_type(object_name: str):
    info = minio_client.stat_object(BUCKET_NAME, object_name)
    return info.content_type

def get_file(object_name: str):
    info = minio_client.stat_object(BUCKET_NAME, object_name)
    total_size = info.size
    offset = 0
    while True:
        response = minio_client.get_object(
            BUCKET_NAME, 
            object_name, 
            offset=offset, 
            length=2048
        )
        yield response.read()
        offset = offset + 2048
        if offset >= total_size:
            break