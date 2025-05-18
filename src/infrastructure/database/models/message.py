from sqlmodel import Field, DateTime
from sqlalchemy import select, update, func
from datetime import datetime
from typing import Dict, Any, Union
from uuid import UUID

from ..table_model import TableModel
from ..database import db


class Message(TableModel, table=True):
    __tablename__ = "message_table"
    
    chat_id: UUID = Field(foreign_key="chat_table.id")
    from_user_id: UUID = Field(foreign_key="user_table.id")
    text: str
    created_at: datetime = DateTime()
    attachment: Union[str, None] = Field(default=None)
    is_read: bool = Field(default=False)
    

    @staticmethod
    async def last(
        chat_id: UUID
    ) -> 'Message':
        query = (
            select(__class__)
            .where(__class__.chat_id == chat_id)
            .order_by(__class__.created_at.desc())
            .limit(1)
        )

        return (await db.execute(query)).scalars().first()
    

    @staticmethod
    async def unread_count(
        chat_id: UUID
    ) -> int:
        query = (
            select(func.count(__class__.id))
            .where(__class__.chat_id == chat_id)
        )

        return (await db.execute(query)).scalars().first()
    

    @staticmethod
    async def read(
        message_id: UUID
    ) -> 'Message':
        query = (
            update(__class__)
            .where(__class__.id == message_id)
            .values(is_read=True)
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
