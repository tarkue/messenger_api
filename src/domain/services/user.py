from typing import List
from uuid import UUID

from src.domain.dto import user as DTO
from src.infrastructure.database import User
from src.infrastructure.repository import user as repository


async def all(
    current_user: User,
    limit: int = 10, 
    offset: int = 0, 
    search: str = ""
) -> List[DTO.UserOut]:
    users = await repository.user.all(current_user.id, limit, offset, search)
    return [DTO.UserOut.model_validate(user) for user in users]



async def get(user_id: UUID) -> DTO.UserOut:
    user = await repository.user.get(user_id)
    return DTO.UserOut.model_validate(user)


def me(user: User) -> DTO.UserOut:
    return DTO.UserOut.model_validate(user)
