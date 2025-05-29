from typing import Optional

from pydantic import UUID4, BaseModel, Field, PastDatetime


class SendMessageDTO(BaseModel):
    to_user_id: UUID4
    text: str = Field(examples=["Hello, world!"])
    createdAt: PastDatetime
    attachment: Optional[str] = None
    