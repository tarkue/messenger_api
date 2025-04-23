from sqlmodel import Field
from sqlalchemy import ColumnExpressionArgument, func, select
from typing import TypeVar, Type, List
from uuid import UUID

from .user import User
from .message import Message
from ..table_model import TableModel
from ..database import db


class Chat(TableModel, table=True):
    __tablename__ = "chat_table"
    
    from_user_id: UUID = Field(foreign_key="user_table.id")
    to_user_id: UUID = Field(foreign_key="user_table.id")


    @staticmethod
    async def find(
        user_id: UUID, 
        limit: int = 10, 
        offset: int = 0,
        search: str = "",
    ) -> List['Chat']:
        query = (
            select(__class__)
            .join(User, User.id == __class__.from_user_id)
            .where(__class__.to_user_id == user_id)
            .limit(limit)
            .offset(offset)
        )

        if search != "":
            query = query.where(func.lower(User.name).like(f'%{search}%'.lower()))

        return (await db.execute(query)).scalars().all()
    

    @staticmethod
    async def exists(*whereclauses: ColumnExpressionArgument) -> bool:
        return await __class__._exists(*whereclauses)


    async def last_message(self) -> Message:
        return await Message.last(self.id)
    

    async def unread_count(self) -> int:
        return await Message.unread_count(self.id)
