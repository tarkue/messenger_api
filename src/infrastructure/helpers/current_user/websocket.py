from fastapi import WebSocket

from src.infrastructure.database import User
from src.infrastructure.helpers.current_user.get import get_current_user


async def get_user_from_websocket(websocket: WebSocket) -> User:
    await websocket.accept()
    token = websocket.headers.get("Authorization")
    if token is None:
        return await websocket.close(1003, "Unauthorized.")
    
    user = await get_current_user(token.split(" ")[1])
    return user
