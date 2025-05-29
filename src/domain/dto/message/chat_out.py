from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field

from src.infrastructure.database import Chat
from src.infrastructure.repository import message as repository

from .message_out import MessageOut


class ChatOut(BaseModel):
    id: UUID
    name: str
    lastMessage: Union[MessageOut, None] = Field(default=None)
    newMessagesCount: int


    @classmethod
    async def from_orm(cls, chat: Chat, user_id: UUID):
        if chat.toUserId == user_id:
            other_user = await repository.user.get(chat.fromUserId)
        else:
            other_user = await repository.user.get(chat.toUserId)

        last_message_from_db = await chat.last_message()
        if last_message_from_db:
            last_message = MessageOut(
                **last_message_from_db.model_dump()
            )
        else: last_message = None
        newMessagesCount = await chat.unread_count(user_id)

        if last_message is None:
            return None
        
        return cls(
            id=other_user.id, 
            name=other_user.name, 
            lastMessage=last_message, 
            newMessagesCount=newMessagesCount
        )
