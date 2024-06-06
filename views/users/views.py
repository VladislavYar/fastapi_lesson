from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from views.users.schemas import UserSchema, UserSchemaIn
from views.users import crud
from core.models import User


router = APIRouter(tags=["Users"])


@router.get(
        "/",
        response_model=list[UserSchema],
        )
async def get_users_list(
        session: AsyncSession = Depends(db_helper.get_session_dependency),
        ) -> list[User]:
    return await crud.get_users(session)


@router.post(
        "/",
        response_model=UserSchema,
        )
async def create_user(
        data_create: UserSchemaIn,
        session: AsyncSession = Depends(db_helper.get_session_dependency),
        ) -> User:
    return await crud.create_user(session, data_create)


@router.get(
        "/{user_id}",
        response_model=UserSchema,
        )
async def get_user(
    user_id: int,
        session: AsyncSession = Depends(db_helper.get_session_dependency),
     ) -> User:
    user: User | None = await crud.get_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User id{user} not found.",
    )
