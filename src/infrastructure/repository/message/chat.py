from typing import List
from uuid import UUID

from sqlalchemy import and_, or_

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

async def exists_by_user(from_user_id: UUID, to_user_id: UUID) -> bool: 
    return await Chat.exists(
        or_(
            and_(Chat.fromUserId == from_user_id,
                 Chat.toUserId == to_user_id),
            and_(Chat.fromUserId == to_user_id,
                 Chat.toUserId == from_user_id)
        )
    )

async def get(chatId: UUID) -> Chat:
    return await Chat._first(Chat.id == chatId)


async def get_by_user(fromUserId: UUID, toUserId: UUID) -> Chat: 
    return await Chat._first(
        or_(Chat.fromUserId == fromUserId, 
            Chat.fromUserId == toUserId)
    )


async def create(fromUserId: UUID, toUserId: UUID):
    return await Chat._create(
        fromUserId=fromUserId, 
        toUserId=toUserId
    )
