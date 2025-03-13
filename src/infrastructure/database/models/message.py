from sqlmodel import Field, DateTime
from datetime import datetime
from uuid import UUID

from ..table_model import TableModel


class Message(TableModel):
    __tablename__ = "user"
    
    chat_id: UUID = Field(foreign_key="chat.id")
    from_user_id: UUID = Field(foreign_key="user.id")
    text: str
    created_at: datetime = DateTime()
    is_read: bool = Field(default=False)
    