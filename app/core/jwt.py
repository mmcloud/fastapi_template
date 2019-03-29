from datetime import datetime, timedelta
import jwt

from core import config

ALGORITHM = "HS256"
access_token_jwt_subject = "access"


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    message = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    message.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded  = jwt.encode(message, config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded