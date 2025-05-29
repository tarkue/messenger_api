from datetime import datetime, timedelta, timezone
from typing import Dict, Union
from uuid import UUID

from jose import jwt

from src.infrastructure.config import env

from .token import Token


class TokenFactory:
    def __init__(
        self, 
        user_id: UUID, 
        *, 
        tokenType: str = "bearer", 
        token_expire: Union[timedelta] = timedelta(hours=8),
        algorithm: str = 'HS256'
    ) -> None:
        self.__user_id = user_id
        self.__tokenType = tokenType
        self.__token_expire = token_expire
        self.__algorithm = algorithm


    def create(self) -> Token:
        return Token(
            accessToken=self.__accessToken, 
            tokenType=self.__tokenType
        )
    
    @property
    def __accessToken(self):
        return self.__generate_accessToken(
            data=self.__generate_data(), 
            expires_delta=self.__token_expire
        )


    def __generate_accessToken(
        self, 
        data: Dict[str, str], 
        expires_delta: Union[timedelta]
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + expires_delta

        to_encode.update({"exp": expire})
        token = jwt.encode(
            to_encode, 
            key=env.app.jwt_secret, 
            algorithm=self.__algorithm
        )
        
        return token
    
    
    def __generate_data(self) -> Dict[str, str]:
        return {"sub": str(self.__user_id)}
