from typing import Any, Callable, Dict, List

from sqlalchemy import ColumnExpressionArgument, func
from sqlmodel import Field

from ..table_model import TableModel


class User(TableModel, table=True):
    __tablename__ = "user_table"
    
    name: str = Field()
    username: str = Field(unique=True)
    password: str = Field(min_length=8)


    @staticmethod
    async def create(
        name: str, 
        username: str, 
        password: str
    ):
        return await __class__._create(
            name=name, 
            username=username, 
            password=password
        )
    

    @staticmethod
    async def update(
        username: str, 
        values: Dict[Any, Any]
    ):
        return await __class__._update(
            User.username == username, 
            values
        )


    @staticmethod
    async def exists(*whereclauses: ColumnExpressionArgument):
        return await __class__._exists(*whereclauses)
    
    
    async def check_password(
        self,
        password_checker: Callable[[str], bool]
    ) -> bool:
        return password_checker(self.password)

    
    @staticmethod
    async def first(
        *whereclauses: ColumnExpressionArgument
    ): 
        return await __class__._first(*whereclauses)
    

    @staticmethod
    async def find(
        limit: int = 10, 
        offset: int = 0,
        search: str = None,
        *whereclauses: ColumnExpressionArgument,
    ):
        filters = [*whereclauses]
        if search is not None and search != "":
            filters.append(func.lower(User.name).like(f'%{search}%'.lower()))
        return await __class__._find(
            filters, 
            (User.id, User.name),
            limit, 
            offset
        )
    