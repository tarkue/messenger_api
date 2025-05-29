from datetime import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class MessageOut(BaseModel):
    model_config = {'from_attributes': True}

    id: UUID
    fromUserId: UUID
    isRead: bool
    text: str
    attachment: Union[str, None] = Field(default=None)
    createdAt: datetime