from fastapi import APIRouter, Body, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from src.domain.dto import auth as DTO
from src.domain.services import auth as service
from src.infrastructure.helpers.token import Token


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token: 
    dto = DTO.LoginDTO(
        username=form_data.username, 
        password=form_data.password
    )
    return await service.login(dto)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(dto: DTO.RegisterDTO = Body(...)) -> None: 
    return await service.register(dto)


@router.post("/restore-password")
async def restore_password(dto: DTO.RestorePasswordDTO = Body(...)) -> None: 
    return await service.restore_password(dto)


@router.post("/change-password")
async def change_password(dto: DTO.ChangePasswordDTO = Body(...)) -> None: 
    return await service.change_password(dto)
