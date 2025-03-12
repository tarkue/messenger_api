from sqlmodel import Field
from sqlalchemy import ColumnExpressionArgument
from typing import Callable, TypeVar, Type, Union, Dict, Any

from ..table_model import TableModel


_T = TypeVar("_T", bound='User')


class User(TableModel):
    __tablename__ = "user"
    
    name: str = Field()
    username: str = Field()
    password: str = Field(min_length=8)


    @classmethod
    async def create(
        cls: Type[_T], 
        name: str, 
        username: str, 
        password: str
    ) -> _T:
        return await super().create(
            name=name, 
            username=username, 
            password=password
        )
    

    @classmethod
    async def update(
        cls: Type[_T], 
        username: str, 
        values: Dict[Any, Any]
    ):
        return await super().update(
            User.username == username, 
            values
        )


    @staticmethod
    async def exists(username: str) -> bool:
        return await __class__.exists(username=username)
    
    
    async def check_password(
        self,
        password_checker: Callable[[str], bool]
    ) -> bool:
        return password_checker(self.password)

    
    @classmethod
    async def first(
        cls: Type[_T], 
        **whereclauses: ColumnExpressionArgument
    ) -> Union[_T, None]: 
        return await super().first(cls, **whereclauses)