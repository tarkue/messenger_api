from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MessageOut(BaseModel):
    id: UUID
    from_user_id: UUID
    is_read: bool
    text: str
    created_at: datetime