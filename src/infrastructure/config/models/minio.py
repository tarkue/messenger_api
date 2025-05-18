from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT


class Minio(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='MINIO_', **CONFIG_DEFAULT)

    user: str
    password: str

    url: str
    port: str
