from fastapi import APIRouter, status
from uuid import UUID

from src.domain.dto import message as DTO
from src.infrastructure.helpers import CurrentUser


router = APIRouter(
    prefix="/message",
    tags=["message"],
)


@router.get("/")
async def get_all_chats(
    user: CurrentUser,
    limit: int = 10,
    offset: int = 0,
    search: str = "",
): ...


@router.get("/{chat_id}")
async def get_messages_in_chat(user: CurrentUser, chat_id: UUID): ...


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_message(user: CurrentUser, dto: DTO.CreateMessageDTO): ...