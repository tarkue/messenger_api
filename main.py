import uvicorn

from src.application.app import app
from src.infrastructure.config import env


if __name__ == "__main__":
    uvicorn.run(
        app, 
        host=env.app.host, 
        port=env.app.port
    )
