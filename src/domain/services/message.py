from uuid import UUID
from fastapi import WebSocket
from typing import List

from src.domain.dto import message as DTO
from src.infrastructure.repository import message as repository
from src.infrastructure.database import User
from src.infrastructure.errors.message import (
    ChatNotFoundError, 
    MessageNotFoundError,
    InvalidTimeError
)


async def all(
    user: User, 
    limit: int = 10, 
    offset: int = 0, 
    search: str = ""
) -> List[DTO.ChatOut]:
    chats_out = []
    chats = await repository.chat.all(
        user.id, 
        limit, 
        offset, 
        search
    )
    for chat in chats:
        chat_out = await DTO.ChatOut.from_orm(chat)
        chats_out.append(chat_out)

    return chats_out


async def get(
    user: User,
    chat_id: UUID,
    limit: int = 10,
    offset: int = 0
) -> List[DTO.MessageOut]:
    if not await repository.chat.exists(chat_id, user.id):
        raise ChatNotFoundError()
    
    return await repository.message.get(chat_id, limit, offset)


async def read(
    user: User,
    message_id: UUID
) -> None:
    if not await repository.message.exists(message_id, user.id):
        raise MessageNotFoundError()
    
    await repository.message.read(message_id)


async def send(
    user: User, 
    dto: DTO.SendMessageDTO
) -> UUID:
    if not await repository.user.exists_by_id(dto.to_user_id):
        raise ChatNotFoundError()
    
    if not await repository.chat.exists(user.id, dto.to_user_id):
        await repository.chat.create(user.id, dto.to_user_id)
    
    chat = await repository.chat.get(user.id, dto.to_user_id)
    last_message = await repository.message.last(chat.id)

    if last_message and last_message.created_at > dto.created_at:
        raise InvalidTimeError()

    message = await repository.message.create(
        chat_id=chat.id, 
        from_user_id=user.id,
        **dto.model_dump(exclude=["to_user_id"])
    )

    await repository.message.update_loop.emit(
        dto.to_user_id,
        message
    )

    return chat.id


async def subscribe(user: User, websocket: WebSocket):
    session_id = repository.message.update_loop.subscribe(user.id)
    loop = repository.message.update_loop.loop(user.id, session_id)
  
    async for message in loop:
        try:
            await websocket.send_json(message.model_dump_json())
        except Exception:
            break

    repository.message.update_loop.unsubscribe(user.id, session_id)
    