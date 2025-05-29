from pydantic import BaseModel, EmailStr, Field, field_validator


class RegisterDTO(BaseModel):
    name: str = Field(examples=["John Doe", "Jane Doe"])
    username: EmailStr = Field(examples=["Tb7Jv@example.com", "qR4tW@example.com"])
    password: str = Field(examples=["password", "password123"], min_length=8)
    confirmPassword: str = Field(examples=["password", "password123"], min_length=8)

    @field_validator("confirmPassword")
    def password_match(cls, confirmPassword: str, values) -> str:
        if confirmPassword != values.data["password"]:
            raise ValueError("passwords do not match")
        
        return confirmPassword