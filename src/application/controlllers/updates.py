from fastapi import APIRouter, WebSocket
from typing import List

from src.domain.dto import message as DTO
from src.domain.services import message as service
from src.infrastructure.helpers import CurrentUserFromWebsocket


router = APIRouter(
    prefix="/updates",
    tags=["updates"],
)


@router.websocket("/")
async def update(
    user: CurrentUserFromWebsocket, 
    websocket: WebSocket
) -> List[DTO.MessageOut]:
    await service.subscribe(user, websocket)
