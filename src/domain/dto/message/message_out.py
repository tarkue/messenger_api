from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class MessageOut(BaseModel):
    id: UUID
    fromUserId: UUID
    isRead: bool
    text: str
    createdAt: datetime