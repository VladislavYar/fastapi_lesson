from typing import Annotated

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from views.users.schemas import UserSchema, UserCreateSchema, UserUpdateSchema
from views.users import crud
from core.models import User
from utils.email_sender import send_email
from views.users.dependencies import get_user_by_id_or_raise
from common.dependencies import PermissionRequired


router = APIRouter(tags=["Users"])


@router.get(
        "/",
        response_model=list[UserSchema],
        dependencies=[
            Depends(PermissionRequired("USERS_GET")),
        ]
        )
async def get_users_list(
        session: Annotated[
            AsyncSession, Depends(db_helper.get_session_dependency)
            ],
        ) -> list[User]:
    return await crud.get_users(session)


@router.post(
        "/",
        response_model=UserSchema,
        dependencies=[
            Depends(PermissionRequired("USERS_CREATE")),
        ]
        )
async def create_user(
        background_tasks: BackgroundTasks,
        data_create: UserCreateSchema,
        session: Annotated[
            AsyncSession, Depends(db_helper.get_session_dependency)
            ],
        ) -> User:
    user = await crud.create_user(session, data_create)
    background_tasks.add_task(send_email, user.email, "Test", "Test text")
    return user


@router.get(
        "/{user_id}",
        response_model=UserSchema,
        )
async def get_user(
        session: Annotated[
            AsyncSession, Depends(db_helper.get_session_dependency)
            ],
        user: User = Depends(get_user_by_id_or_raise),
     ) -> User:
    return user


@router.patch(
        "/{user_id}",
        response_model=UserSchema,
        )
async def update_user(
        session: Annotated[
            AsyncSession, Depends(db_helper.get_session_dependency)
            ],
        data_update: UserUpdateSchema,
        user: User = Depends(get_user_by_id_or_raise),
     ) -> User:
    return await crud.update_user(session, user, data_update)
