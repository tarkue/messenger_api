from fastapi import APIRouter

from src.infrastructure.helpers import CurrentUser


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get("/me")
async def get_info_about_me(user: CurrentUser): ...