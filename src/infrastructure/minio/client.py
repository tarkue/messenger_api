from minio import Minio
from src.infrastructure.config import env

# Initialize MinIO client
minio_client = Minio(
    env.minio.url,
    access_key=env.minio.user,
    secret_key=env.minio.password,
    secure=False
)