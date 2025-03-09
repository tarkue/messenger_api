from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT


class App(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_', **CONFIG_DEFAULT)

    host: str
    port: int

    title: str
    description: str
    version: str

    jwt_secret: str
