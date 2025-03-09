from pydantic import BaseModel, Field, EmailStr


class LoginDTO(BaseModel):
    username: EmailStr = Field(examples=["Tb7Jv@example.com", "qR4tW@example.com"])
    password: str = Field(examples=["password", "password123"], min_length=8)
   