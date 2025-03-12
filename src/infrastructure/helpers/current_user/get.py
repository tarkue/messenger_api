from typing_extensions import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends

from ..token.token import TokenData
from src.infrastructure.database import User
from src.infrastructure.config import env
from src.infrastructure.errors.auth import NotValidateCredentialsError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    access_token: Annotated[str, Depends(oauth2_scheme)]
) -> User:
    """
    Gets current user
    :param access_token: token that we decode to recognize the user
    :return: current user if token is valid
    """
    try:
        token_data = decode(access_token)
        return await User.first(User.id == token_data.user_id)
    except Exception:
        raise NotValidateCredentialsError()
    

def decode(token: str, *, algorithms='HS256') -> TokenData:
    decoded_data = jwt.decode(
        token, 
        key=env.app.jwt_secret, 
        algorithms=algorithms
    )
    return decoded_data
