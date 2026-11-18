from datetime import datetime, timedelta, timezone
from jose import jwt
from pwdlib import PasswordHash
from app.config import settings

#password hashing system
password_hash = PasswordHash.recommended()

#Hash password
def hash_password(password: str):

    return password_hash.hash(password)

#verify password
def verify_password(plan_password: str, hashed_password: str):

    return password_hash.verify(
        plain_password,
        hashed_passsword
    )

#Ceate JWT access token
def create_access_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token