import uuid
from typing import TypeVar, Generic, Union, Type
from sqlalchemy import select, ColumnExpressionArgument, ColumnClause
from sqlmodel import SQLModel, Field

from ..database import db


T = TypeVar("T", bound=ColumnClause)


class TableModel(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)

    @classmethod
    async def create(cls, **kwargs) -> T:
        instance = cls(**kwargs)
        db.add(instance)
        await db.commit_rollback()

        return instance
    
    
    @classmethod
    async def first(
        cls: Type[T], 
        **whereclause: ColumnExpressionArgument
    ) -> Union[T, None]:
        query = select(cls).where(**whereclause).limit(1)
        executed = (await db.execute(query)).first()
        if executed is not None:
            return executed[0]

        return None


    @classmethod
    async def exists(
        cls: T, 
        **whereclause: ColumnExpressionArgument
    ) -> bool:
        query = select(1).where(**whereclause).limit(1)
        executed = (await db.execute(query)).first()

        return executed is not None
