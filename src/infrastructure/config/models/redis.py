from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT


class Redis(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='REDIS_', **CONFIG_DEFAULT)

    url: str
