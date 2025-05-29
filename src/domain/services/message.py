from typing import List
from uuid import UUID

from fastapi import WebSocket
from fastapi.encoders import jsonable_encoder

from src.domain.dto import message as DTO
from src.infrastructure.database import User
from src.infrastructure.errors.message import (ChatNotFoundError,
                                               InvalidTimeError,
                                               MessageNotFoundError)
from src.infrastructure.repository import message as repository


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
        chat_out = await DTO.ChatOut.from_orm(chat, user.id)
        if chat_out is None:
            continue
        chats_out.append(chat_out)

    return chats_out[::-1]


async def get(
    user: User,
    userId: UUID,
    limit: int = 10,
    offset: int = 0
) -> List[DTO.MessageOut]:
    if not await repository.chat.exists_by_user(user.id, userId):
        await repository.chat.create(user.id, userId)
    
    chat = await repository.chat.get_by_user(user.id, userId)
   
    messages = await repository.message.get(chat.id, limit, offset)

    for i in range(len(messages)):
        if messages[i].fromUserId == user.id:
            new_message = DTO.MessageOut.model_validate(messages[i])
            new_message.isRead = True
            messages[i] = new_message


    return messages[::-1]


async def read(
    user: User,
    message_id: UUID
) -> None:
    if not await repository.message.exists(message_id):
        raise MessageNotFoundError()
    
    message = await repository.message.get_by_id(message_id)
    chat = await repository.chat.get(message.chatId)

    if chat.fromUserId != user.id and chat.toUserId != user.id:
        raise MessageNotFoundError()
    
    await repository.message.read(message_id)


async def send(
    user: User, 
    dto: DTO.SendMessageDTO
) -> UUID:
    if not await repository.user.exists_by_id(dto.toUserId):
        raise ChatNotFoundError()
    
    if not await repository.chat.exists_by_user(user.id, dto.toUserId):
        await repository.chat.create(user.id, dto.toUserId)
    
    chat = await repository.chat.get_by_user(user.id, dto.toUserId)
    last_message = await repository.message.last(chat.id)

    dto.createdAt = dto.createdAt.replace(tzinfo=None)

    if last_message and last_message.createdAt > dto.createdAt:
        raise InvalidTimeError()

    message = await repository.message.create(
        chatId=chat.id, 
        fromUserId=user.id,
        **dto.model_dump(exclude=["toUserId"])
    )

    await repository.message.update_loop.emit(
        dto.toUserId,
        message
    )

    return message.id


async def subscribe(user: User, websocket: WebSocket):
    session_id = repository.message.update_loop.subscribe(user.id)
    loop = repository.message.update_loop.loop(user.id, session_id)
  
    async for message in loop:
        try:
            await websocket.send_json(jsonable_encoder(
                message.model_dump())
            )
        except Exception:
            break

    repository.message.update_loop.unsubscribe(user.id, session_id)
    