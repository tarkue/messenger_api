from typing import List
from uuid import UUID

from src.domain.dto import user as DTO
from src.infrastructure.repository import user as repository
from src.infrastructure.database import User


async def all(
    limit: int = 10, 
    offset: int = 0, 
    search: str = ""
) -> List[DTO.UserOut]:
    users = await repository.user.all(limit, offset, search)
    return [DTO.UserOut.model_validate(user) for user in users]



async def get(user_id: UUID) -> DTO.UserOut:
    user = await repository.user.get(user_id)
    return DTO.UserOut.model_validate(user)


def me(user: User) -> DTO.UserOut:
    print(user)
    return DTO.UserOut.model_validate(user)
