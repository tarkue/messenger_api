from uuid import UUID, uuid4
from typing import TypeVar, Type, Dict, List
from sqlalchemy import select, update, ColumnExpressionArgument
from sqlmodel import SQLModel, Field

from ..database import db


_T = TypeVar("_T", bound='TableModel')


class TableModel(SQLModel):
    id: UUID = Field(
        default_factory=uuid4, 
        primary_key=True
    )

    @classmethod
    async def _create(cls: Type[_T], **kwargs) -> _T:
        instance = cls(**kwargs)
        db.add(instance)
        await db.commit_rollback()

        return instance
    
    
    @classmethod
    async def _first(
        cls: Type[_T], 
        *whereclause: ColumnExpressionArgument
    ) -> _T:
        query = select(cls).where(*whereclause).limit(1)
        executed = (await db.execute(query)).first()
        if executed is not None:
            return executed[0]

        return None

    @classmethod
    async def _update(
        cls: Type[_T], 
        whereclauses: ColumnExpressionArgument,
        values: Dict[str, str]
    ) -> None:
        stmt = (update(cls)
                .where(*whereclauses)
                .values(**values))
        await db.execute(stmt)
        await db.commit_rollback()
    


    @classmethod
    async def _exists(
        cls: Type[_T], 
        *whereclause: ColumnExpressionArgument
    ) -> bool:
        query = select(1).where(*whereclause).limit(1)
        executed = (await db.execute(query)).first()

        return executed is not None

    @classmethod
    async def _find(
        cls: Type[_T], 
        whereclauses: ColumnExpressionArgument = [],
        columns: List[ColumnExpressionArgument] = [],
        limit: int = 10, 
        offset: int = 0
    ) -> List[_T]:
        query = (select(*columns if len(columns) > 0 else cls)
                 .limit(limit)
                 .offset(offset)
        )

        if len(whereclauses) > 0:
            query = query.where(*whereclauses) 
            
        return (await db.execute(query)).all()
    