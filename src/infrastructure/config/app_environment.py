from dataclasses import dataclass
from .models import *


@dataclass
class EnvironmentConfig:
    app: App = App()
    database: Database = Database()
    redis: Redis = Redis()

env = EnvironmentConfig()