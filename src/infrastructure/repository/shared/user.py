__all__ = (
    "find_by_credentials", 
    "exists", 
    "create", 
    "get", 
    "all"
)

from typing import List
from uuid import UUID

from src.infrastructure.database import User
from src.infrastructure.errors.auth import IncorrectCredentialsError
from src.infrastructure.helpers import check_password


async def find_by_credentials(credentials: User) -> User:
    user = await User.first(User.username == credentials.username)

    if not check_password(credentials.password, user.password): 
        raise IncorrectCredentialsError()
    
    return user


async def exists_by_id(user_id: str) -> bool:
    return await User.exists(User.id == user_id)


async def exists(username: str) -> bool:
    return await User.exists(User.username == username)


async def create(credentials: User) -> User:
    return await User.create(**credentials.model_dump(
        exclude=["confirmPassword"]
    ))


async def get(user_id: UUID) -> User:
    return await User.first(User.id == user_id)


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
