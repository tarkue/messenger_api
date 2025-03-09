from pydantic import BaseModel, Field, EmailStr


class RestorePasswordDTO(BaseModel):
    username: EmailStr = Field(examples=["Tb7Jv@example.com", "qR4tW@example.com"])
    