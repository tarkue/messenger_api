from typing import List
from uuid import UUID

from .update_loop import UpdateLoop
from src.infrastructure.database import Message


update_loop = UpdateLoop()


async def get(chat_id: UUID, limit = 10, offset = 0) -> List[Message]: 
    return await Message.find(
        [Message.chat_id == chat_id],
        [
            Message.id,
            Message.from_user_id, 
            Message.is_read,
            Message.created_at, 
            Message.text, 
        ],
        limit,
        offset
    )


async def last(chat_id: UUID) -> Message: 
    return await Message.last(chat_id)


async def exists(message_id: UUID, user_id: UUID) -> bool: 
    return await Message.exists(
        Message.id == message_id,
        Message.from_user_id == user_id
    )


async def read(message_id: UUID) -> None:
    await Message.read(message_id)


async def create(**kwargs) -> Message: 
    return await Message.create(**kwargs)
