from uuid import UUID

from pydantic import BaseModel


class Token(BaseModel):
    accessToken: str
    tokenType: str


class TokenData(BaseModel):
    id: UUID
