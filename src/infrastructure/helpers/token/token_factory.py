from jose import jwt
from typing import Union, Dict
from uuid import UUID
from datetime import datetime, timedelta, timezone

from .token import Token
from src.infrastructure.config import env


class TokenFactory:
    def __init__(
        self, 
        user_id: UUID, 
        *, 
        token_type: str = "bearer", 
        token_expire: Union[timedelta] = timedelta(hours=8),
        algorithm: str = 'HS256'
    ) -> None:
        self.__user_id = user_id
        self.__token_type = token_type
        self.__token_expire = token_expire
        self.__algorithm = algorithm


    def create(self) -> Token:
        return Token(
            access_token=self.__access_token, 
            token_type=self.__token_type
        )
    
    @property
    def __access_token(self):
        return self.__generate_access_token(
            data=self.__generate_data(), 
            expires_delta=self.__token_expire
        )


    def __generate_access_token(
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
