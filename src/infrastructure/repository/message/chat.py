from typing import List
from uuid import UUID

from src.infrastructure.database import Chat


async def all(
    user_id: UUID, 
    limit: int = 10, 
    offset: int = 0, 
    search: str = ""
) -> List[Chat]:
    return await Chat.find(
        user_id, 
        limit=limit,
        offset=offset, 
        search=search
    )


async def exists(chatId: UUID, user_id: UUID) -> bool: 
    return await Chat.exists(
        Chat.id == chatId,
        Chat.fromUserId == user_id,
    )


async def get(fromUserId: UUID, toUserId: UUID) -> Chat: 
    return await Chat._first(
        Chat.fromUserId==fromUserId, 
        Chat.toUserId == toUserId
    )


async def create(fromUserId: UUID, toUserId: UUID):
    return await Chat._create(
        fromUserId=fromUserId, 
        toUserId=toUserId
    )
