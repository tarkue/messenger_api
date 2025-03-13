from sqlmodel import Field, DateTime
from sqlalchemy import select, update, func
from datetime import datetime
from typing import TypeVar, Type
from uuid import UUID

from ..table_model import TableModel
from ..database import db


_T = TypeVar("_T", bound='Message')


class Message(TableModel):
    __tablename__ = "user"
    
    chat_id: UUID = Field(foreign_key="chat.id")
    from_user_id: UUID = Field(foreign_key="user.id")
    text: str
    created_at: datetime = DateTime()
    is_read: bool = Field(default=False)
    

    @classmethod
    def last(
        cls: Type[_T], 
        chat_id: UUID
    ) -> _T:
        query = (
            select(cls)
            .where(cls.chat_id == chat_id)
            .order_by(cls.created_at.desc())
            .limit(1)
        )

        return (db.execute(query)).scalars().first()
    

    @classmethod
    async def unread_count(
        cls: Type[_T], 
        chat_id: UUID
    ) -> int:
        query = (
            select(func.count(cls.id))
            .where(cls.chat_id == chat_id)
        )

        return (await db.execute(query)).scalars().first()
    

    @classmethod
    async def read(
        cls: Type[_T], 
        message_id: UUID
    ) -> _T:
        query = (
            update(cls)
            .where(cls.id == message_id)
            .values(is_read=True)
        )

        await db.execute(query)
        await db.commit_rollback()
