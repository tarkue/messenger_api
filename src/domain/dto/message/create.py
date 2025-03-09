from pydantic import UUID4, PastDatetime, BaseModel, Field, field_validator
from datetime import datetime, timedelta


class CreateMessageDTO(BaseModel):
    chat_id: UUID4
    text: str = Field(examples=["Hello, world!"])
    created_at: PastDatetime

    @field_validator("created_at")
    def validate_created_at(cls, value: datetime) -> datetime:
        now = datetime.now()
        if (now - value) > timedelta(seconds=12):
            raise ValueError("created_at is too old")
        
        return value