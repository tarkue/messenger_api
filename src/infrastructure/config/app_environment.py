from dataclasses import dataclass
from .models import *


@dataclass
class EnvironmentConfig:
    app: App = App()
    mail: Mail = Mail()
    database: Database = Database()
    redis: Redis = Redis()
    minio: Minio = Minio()

env = EnvironmentConfig()
