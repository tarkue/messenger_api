from typing import List
from uuid import UUID

from sqlalchemy import and_

from src.infrastructure.database import Message

from .update_loop import UpdateLoop

update_loop = UpdateLoop()


async def get(chatId: UUID, limit = 10, offset = 0) -> List[Message]: 
    return await Message.find(
        [Message.chatId == chatId],
        [
            Message.id,
            Message.fromUserId, 
            Message.isRead,
            Message.createdAt, 
            Message.text, 
            Message.attachment
        ],
        limit,
        offset
    )

async def get_by_id(message_id: UUID) -> Message:
    return await Message._first(Message.id == message_id)

async def last(chatId: UUID) -> Message: 
    return await Message.last(chatId)


async def exists(message_id: UUID) -> bool:
    return await Message.exists(
        Message.id == message_id
    )


async def read(message_id: UUID) -> None:
    await Message.read(message_id)


async def create(**kwargs) -> Message: 
    return await Message.create(**kwargs)
