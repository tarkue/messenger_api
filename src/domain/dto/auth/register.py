from pydantic import BaseModel, Field, EmailStr, field_validator


class RegisterDTO(BaseModel):
    name: str = Field(examples=["John Doe", "Jane Doe"])
    username: EmailStr = Field(examples=["Tb7Jv@example.com", "qR4tW@example.com"])
    password: str = Field(examples=["password", "password123"], min_length=8)
    confirm_password: str = Field(examples=["password", "password123"], min_length=8)

    @field_validator("confirm_password")
    def password_match(cls, confirm_password: str, values) -> str:
        if confirm_password != values.data["password"]:
            raise ValueError("passwords do not match")
        
        return confirm_password