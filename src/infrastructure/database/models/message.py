from datetime import datetime
from typing import Any, Dict, Union
from uuid import UUID

from sqlalchemy import func, select, update
from sqlmodel import DateTime, Field

from ..database import db
from ..table_model import TableModel


class Message(TableModel, table=True):
    __tablename__ = "message_table"
    
    chatId: UUID = Field(foreign_key="chat_table.id")
    fromUserId: UUID = Field(foreign_key="user_table.id")
    text: str
    createdAt: datetime = DateTime()
    attachment: Union[str, None] = Field(default=None)
    isRead: bool = Field(default=False)
    

    @staticmethod
    async def last(
        chatId: UUID
    ) -> 'Message':
        query = (
            select(__class__)
            .where(__class__.chatId == chatId)
            .order_by(__class__.createdAt.desc())
            .limit(1)
        )

        return (await db.execute(query)).scalars().first()
    

    @staticmethod
    async def unread_count(
        chatId: UUID
    ) -> int:
        query = (
            select(func.count(__class__.id))
            .where(__class__.chatId == chatId)
        )

        return (await db.execute(query)).scalars().first()
    

    @staticmethod
    async def read(
        message_id: UUID
    ) -> 'Message':
        query = (
            update(__class__)
            .where(__class__.id == message_id)
            .values(isRead=True)
        )

        await db.execute(query)
        await db.commit_rollback()

    
    @staticmethod
    async def create(**dto: Dict[str, Any]):
        return await __class__._create(**dto)


    @staticmethod
    async def find(whereclauses = ..., columns = ..., limit = 10, offset = 0):
        return await __class__._find(whereclauses, columns, limit, offset)
    

    @staticmethod
    async def exists(*whereclause):
        return await __class__._exists(*whereclause)
