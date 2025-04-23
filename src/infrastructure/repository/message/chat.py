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


async def exists(chat_id: UUID, user_id: UUID) -> bool: 
    return await Chat.exists(
        Chat.id == chat_id,
        Chat.from_user_id == user_id,
    )


async def get(from_user_id: UUID, to_user_id: UUID) -> Chat: 
    return await Chat._first(
        Chat.from_user_id==from_user_id, 
        Chat.to_user_id == to_user_id
    )


async def create(from_user_id: UUID, to_user_id: UUID):
    return await Chat._create(
        from_user_id=from_user_id, 
        to_user_id=to_user_id
    )
