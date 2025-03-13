from pydantic import BaseModel

from .message_out import MessageOut
from src.infrastructure.database import Chat
from src.infrastructure.repository import message as repository


class ChatOut(BaseModel):
    id: str
    name: str
    last_message: MessageOut
    new_messages_count: int


    @classmethod
    async def from_orm(cls, chat: Chat):
        to_user = await repository.user.get(chat.to_user_id)
        last_message = MessageOut.model_validate(await chat.last_message())
        new_messages_count = await chat.unread_count()

        return cls(
            id=chat.id, 
            name=to_user.name, 
            last_message=last_message, 
            new_messages_count=new_messages_count
        )
