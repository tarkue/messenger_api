from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT

from redis_om import get_redis_connection


class Redis(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='REDIS_', **CONFIG_DEFAULT)

    url: str

    @property
    def connection(self):
        return get_redis_connection(url=self.url)
