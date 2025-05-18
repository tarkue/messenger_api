from typing import Optional
from pydantic import UUID4, PastDatetime, BaseModel, Field


class SendMessageDTO(BaseModel):
    to_user_id: UUID4
    text: str = Field(examples=["Hello, world!"])
    created_at: PastDatetime
    attachment: Optional[str] = None
    