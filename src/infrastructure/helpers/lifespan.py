from fastapi import FastAPI
from redis_om import Migrator

from src.infrastructure.database import db
from src.infrastructure.config import env


async def lifespan(app: FastAPI):
    db.init(env.database.url)
    await db.create_all()
    Migrator().run()
    yield
    await db.close()
