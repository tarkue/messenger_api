from fastapi import WebSocket

from src.infrastructure.database import User
from src.infrastructure.helpers.current_user.get import get_current_user


async def get_user_from_websocket(websocket: WebSocket) -> User:
    await websocket.accept()
    while True:
        token = await websocket.receive_text()
        user = await get_current_user(token)
        return user
