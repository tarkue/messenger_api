__all__ = ("app",)

from fastapi import FastAPI

from .controlllers import routers
from src.infrastructure.config import env
from src.infrastructure.helpers import merge_routers


app = FastAPI(
    title=env.app.title,
    description=env.app.description,
    version=env.app.version,
)
merged_router = merge_routers(routers)
app.include_router(merged_router)
