from .client import minio_client


# Bucket name for storing files
BUCKET_NAME = "messenger-files"

async def ensure_bucket():
    """Ensure the bucket exists"""
    try:
        if not minio_client.bucket_exists(BUCKET_NAME):
            minio_client.make_bucket(BUCKET_NAME)
    except Exception as e:
        print(f"Error ensuring bucket exists: {e}")
        raise