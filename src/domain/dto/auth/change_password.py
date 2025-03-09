from pydantic import BaseModel, Field, field_validator


class ChangePasswordDTO(BaseModel):
    restore_token: str
    password: str = Field(examples=["password", "password123"], min_length=8)
    confirm_password: str = Field(examples=["password", "password123"], min_length=8)

    @field_validator("confirm_password")
    def password_match(cls, value: str, values: dict[str, str]) -> str:
        if "password" in values and value != values["password"]:
            raise ValueError("passwords do not match")
        
        return value
