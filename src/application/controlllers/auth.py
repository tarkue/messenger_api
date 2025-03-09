from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from src.domain.dto import auth as DTO
from src.domain.services import auth as service


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
): 
    dto = DTO.LoginDTO(**form_data)
    return service.login(dto)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(dto: DTO.RegisterDTO): 
    return service.register(dto)


@router.post("/restore-password")
async def restore_password(dto: DTO.RestorePasswordDTO): 
    return service.restore_password(dto)


@router.post("/change-password")
async def change_password(dto: DTO.ChangePasswordDTO): 
    return service.change_password(dto)
