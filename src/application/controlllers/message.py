from typing import List
from uuid import UUID

from fastapi import APIRouter, Body, status

from src.domain.dto import message as DTO
from src.domain.services import message as service
from src.infrastructure.helpers import CurrentUser

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
)


@router.get("/")
async def get_all_chats_of_user(
    user: CurrentUser,
    limit: int = 10,
    offset: int = 0,
    search: str = "",
) -> List[DTO.ChatOut]: 
    return await service.all(
        user, 
        limit, 
        offset, 
        search
    )


@router.get("/{userId}")
async def get_messages_in_chat(
    user: CurrentUser, 
    userId: UUID,
    limit: int = 10,
    offset: int = 0
) -> List[DTO.MessageOut]: 
    return await service.get(
        user, 
        userId,
        limit,
        offset
    )


@router.patch("/{message_id}/read")
async def mark_messages_as_read(
    user: CurrentUser, 
    message_id: UUID
) -> None: 
    return await service.read(user, message_id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def send_message(
    user: CurrentUser, 
    dto: DTO.SendMessageDTO = Body(...)
) -> None: 
    return await service.send(user, dto)

