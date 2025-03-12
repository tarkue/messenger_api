from src.infrastructure.config import env

from redis_om import JsonModel, Field


class RestorePassword(JsonModel):
    token: str = Field(primary_key=True)
    username: str

    class Meta:
        database = env.redis.connection
