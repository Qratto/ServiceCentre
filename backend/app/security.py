import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta, timezone, datetime
from typing import Annotated

from app.database import get_db
from app.schemas.token import TokenData
from app.config import settings
from app.models import Employee


password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)


async def get_user(username: str, session: AsyncSession):
    result = await session.execute(select(Employee).where(Employee.username == username))
    return result.scalars().first()


async def authenticate_user(username: str, password: str, session: AsyncSession):
    user = await get_user(username, session)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    decode_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return decode_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = await get_user(username, session)
    if user is None:
        raise credentials_exception
    return user