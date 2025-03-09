from src.domain.dto import auth as DTO

from src.domain.helpers.email import EmailSender, RestorePasswordEmail
from src.domain.helpers.hash import hash_password, generate_restore_token
from src.infrastructure.helpers.token import TokenFactory, Token
from src.infrastructure.repository import auth as repository
from src.infrastructure.errors.auth import (
    UserNotFoundError,
    IncorrectCredentialsError, 
    UserAlreadyExistsError
)


async def login(credentials: DTO.LoginDTO) -> Token:
    try:
        user_id = await repository.user.find_by_credentials(credentials)
        return TokenFactory(user_id).create()
    except UserNotFoundError:
        raise IncorrectCredentialsError()
    

async def register(credentials: DTO.RegisterDTO) -> None:
    if await repository.user.exists(credentials.username):
        raise UserAlreadyExistsError()
    
    credentials["password"] = hash_password(credentials["password"])
    await repository.user.create(credentials)


async def change_password(credentials: DTO.ChangePasswordDTO) -> None:
    if not await repository.restore_token.exists(credentials.restore_token):
        raise UserNotFoundError()
    
    credentials["password"] = hash_password(credentials["password"])
    await repository.update_password_by_restore_token(
        credentials.restore_token,
        credentials.password
    )


async def restore_password(credentials: DTO.RestorePasswordDTO) -> None:
    if not await repository.user.exists(credentials):
        raise UserNotFoundError()
    
    restore_token = generate_restore_token()
    await repository.restore_token.remember(credentials, restore_token)

    email = RestorePasswordEmail(credentials["email"], restore_token)
    await EmailSender.send(email)
