from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str = Field(examples=["John Doe", "Jane Doe"])
