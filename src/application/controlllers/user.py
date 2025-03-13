from fastapi import APIRouter
from typing import List

from src.domain.services import user as service
from src.domain.dto import user as DTO
from src.infrastructure.helpers import CurrentUser


router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/")
async def get_all_users(
    user: CurrentUser,
    limit: int = 10,
    offset: int = 0,
    search: str = ""
) -> List[DTO.UserOut]:
    return await service.all(limit, offset, search)


@router.get("/me")
async def get_info_about_me(user: CurrentUser) -> DTO.UserOut:
    return service.me(user)