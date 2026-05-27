from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from datetime import timedelta

from app.database import get_db
from app.models import Employee
from app.schemas.token import Token
from app.config import settings
from app.security import authenticate_user, create_access_token, get_current_user

auth_router = APIRouter(tags=["auth"])

@auth_router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 session: AsyncSession = Depends(get_db)) -> Token:
    user = await authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password")
    access_token_expire = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expire
    )
    return Token(access_token=access_token, token_type="bearer")


@auth_router.get("/users/me")
async def read_users_me(current_user: Annotated[Employee, Depends(get_current_user)]):
    return current_user