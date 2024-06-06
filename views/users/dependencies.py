from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User
from views.users import crud


async def get_user_by_id_or_raise(
    user_id: Annotated[int, Path],
        session: Annotated[
            AsyncSession, Depends(db_helper.get_session_dependency)
            ],
     ) -> User:
    user: User = await crud.get_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User id {user_id} not found.",
    )
