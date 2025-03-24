__all__ = ("app",)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controlllers import routers
from src.infrastructure.config import env
from src.infrastructure.helpers import merge_routers, lifespan


app = FastAPI(
    title=env.app.title,
    description=env.app.description,
    version=env.app.version,
    lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=1728000
)  # add a cors middleware from FastAPI to an app

merged_router = merge_routers(routers)
app.include_router(merged_router)
