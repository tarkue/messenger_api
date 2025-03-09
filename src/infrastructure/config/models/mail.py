from pydantic_settings import BaseSettings, SettingsConfigDict
from .model_config_default import CONFIG_DEFAULT


class Mail(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='MAIL_', **CONFIG_DEFAULT)

    host: str
    port: int

    username: str
    password: str
