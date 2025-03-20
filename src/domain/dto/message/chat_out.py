from pydantic import BaseModel, Field
from uuid import UUID
from typing import Union

from .message_out import MessageOut
from src.infrastructure.database import Chat
from src.infrastructure.repository import message as repository


class ChatOut(BaseModel):
    id: UUID
    name: str
    last_message: Union[MessageOut, None] = Field(default=None)
    new_messages_count: int


    @classmethod
    async def from_orm(cls, chat: Chat):
        to_user = await repository.user.get(chat.to_user_id)
        last_message_from_db = await chat.last_message()
        if last_message_from_db:
            last_message = MessageOut(
                **last_message_from_db.model_dump()
            )
        else: last_message = None
        new_messages_count = await chat.unread_count()

        return cls(
            id=chat.id, 
            name=to_user.name, 
            last_message=last_message, 
            new_messages_count=new_messages_count
        )
