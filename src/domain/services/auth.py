from src.domain.dto import auth as DTO

from src.domain.extension.email import EmailSender, RestorePasswordEmail
from src.domain.helpers.hash import hash_password, generate_restore_token
from src.infrastructure.helpers.token import TokenFactory, Token
from src.infrastructure.repository import auth as repository
from src.infrastructure.errors.auth import (
    UserNotFoundError,
    IncorrectCredentialsError, 
    UserAlreadyExistsError
)


async def login(dto: DTO.LoginDTO) -> Token:
    if not await repository.user.exists(dto.username):
        raise IncorrectCredentialsError()
    
    user = await repository.user.find_by_credentials(dto)
    return TokenFactory(user.id).create()
    

async def register(dto: DTO.RegisterDTO) -> None:
    if await repository.user.exists(dto.username):
        raise UserAlreadyExistsError()

    dto.password = hash_password(dto.password)
    await repository.user.create(dto)


async def change_password(dto: DTO.ChangePasswordDTO) -> None:
    if not await repository.restore_token.exists(dto.restore_token):
        raise UserNotFoundError()
    
    hashed_password = hash_password(dto.password)
    await repository.update_password_by_restore_token(
        dto.restore_token,
        hashed_password
    )


async def restore_password(dto: DTO.RestorePasswordDTO) -> None:
    if not await repository.user.exists(dto.username):
        raise UserNotFoundError()

    token = generate_restore_token()
    await repository.restore_token.remember(dto.username, token)

    email = RestorePasswordEmail(dto.username, token)
    await EmailSender.send(email)
