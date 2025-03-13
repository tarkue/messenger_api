from sqlmodel import Field
from sqlalchemy import func, select
from typing import TypeVar, Type, List
from uuid import UUID

from .user import User
from .message import Message
from ..table_model import TableModel
from ..database import db


_T = TypeVar("_T", bound='Chat')


class Chat(TableModel):
    __tablename__ = "chat"
    
    from_user_id: UUID = Field(foreign_key="user.id")
    to_user_id: UUID = Field(foreign_key="user.id")


    @classmethod
    async def find(
        cls: Type[_T], 
        limit: int = 10, 
        offset: int = 0,
        search: str = "",
    ) -> List[_T]:
        query = (
            select(cls)
            .join(User, User.id == cls.from_user_id)
            .limit(limit)
            .offset(offset)
            .where(func.lower(User.name).like(search.lower))
        )

        return (await db.execute(query)).scalars().all()
    

    async def last_message(self) -> Message:
        return await Message.last(self.id)
    

    async def unread_count(self) -> int:
        return await Message.unread_count(self.id)