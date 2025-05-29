from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, Field


class SendMessageDTO(BaseModel):
    toUserId: UUID4
    text: str = Field(examples=["Hello, world!"])
    createdAt: datetime
    attachment: Optional[str] = None
    