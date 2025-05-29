from typing import List

from fastapi import APIRouter, WebSocket

from src.domain.dto import message as DTO
from src.domain.services import message as service
from src.infrastructure.helpers import CurrentUserFromWebsocket

router = APIRouter(
    prefix="/updates",
    tags=["updates"],
)


@router.websocket("")
async def update(
    websocket: WebSocket,
    user: CurrentUserFromWebsocket, 
) -> None:
    await service.subscribe(user, websocket)
