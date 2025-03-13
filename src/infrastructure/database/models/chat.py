from sqlmodel import Field
from uuid import UUID

from ..table_model import TableModel


class Chat(TableModel):
    __tablename__ = "chat"
    
    from_user_id: UUID = Field(foreign_key="user.id")
    to_user_id: UUID = Field(foreign_key="user.id")
