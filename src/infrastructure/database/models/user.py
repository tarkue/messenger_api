from sqlmodel import Field
from typing import Callable
from uuid import UUID

from ...errors.auth import UserNotFoundError
from ..table_model import TableModel


class User(TableModel):
    __tablename__ = "user"
    
    name: str = Field(index=True)
    username: str = Field(index=True)
    password: str = Field(index=True, min_length=8)


    @classmethod
    async def create(
        cls: 'User', 
        name: str, 
        username: str, 
        password: str
    ) -> 'User':
        return await super().create(
            name=name, 
            username=username, 
            password=password
        )
    

    @staticmethod
    async def exists(username: str) -> bool:
        return await __class__.exists(username=username)
    
    
    @staticmethod
    async def check_password(
        credentials: dict[str, str], 
        password_checker: Callable[[str], bool]
    ) -> 'User':
        user = await __class__.first(username=credentials["username"])

        if user is None:
            raise UserNotFoundError()
        
        return password_checker(user.password)
