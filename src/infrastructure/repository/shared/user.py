__all__ = (
    "find_by_credentials", 
    "exists", 
    "create", 
    "get", 
    "all"
)

from typing import List
from uuid import UUID

from src.infrastructure.errors.auth import IncorrectCredentialsError
from src.infrastructure.database import User
from src.infrastructure.helpers import check_password


async def find_by_credentials(credentials: User) -> User:
    user = await User.first(username=credentials.username)

    if not check_password(credentials.password, user.password): 
        raise IncorrectCredentialsError()
    
    return user


async def exists(username: str) -> bool:
    return await User.exists(username)


async def create(credentials: User) -> User:
    return await User.create(**credentials.model_dump())


async def all(
    limit: int = 10, 
    offset: int = 0, 
    search: str = ""
) -> List[User]:
    return await User.find(
        limit=limit,
        offset=offset, 
        search=search
    )
