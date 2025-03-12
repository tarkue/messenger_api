from pydantic import BaseModel, Field, field_validator


class ChangePasswordDTO(BaseModel):
    restore_token: str
    password: str = Field(examples=["password", "password123"], min_length=8)
    confirm_password: str = Field(examples=["password", "password123"], min_length=8)

    @field_validator("confirm_password", mode="after")
    def password_match(cls, confirm_password: str, values) -> str:
        if confirm_password != values.data["password"]:
            raise ValueError("passwords do not match")
        
        return confirm_password
