from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT


class Database(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='DATABASE_', **CONFIG_DEFAULT)

    host: str
    port: str
    name: str
    user: str
    password: str
