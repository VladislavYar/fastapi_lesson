from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from core.models import User, Post
from views.users.schemas import UserSchemaIn


async def create_user(
        session: AsyncSession,
        data_create: UserSchemaIn,
) -> User:
    user = User(**data_create.model_dump())
    async with session.begin():
        session.add(user)
    return user


async def get_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users


async def get_user_by_id(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def get_user_by_username(session: AsyncSession,
                               username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    result: Result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    return user


async def create_posts_for_user(session: AsyncSession,
                                user: User,
                                *post_titles: str,
                                ) -> list[Post]:
    posts = [
        Post(title=title, author_id=user.id)
        for title in post_titles
    ]
    async with session.begin_nested():
        session.add_all(posts)
    return posts


async def get_posts_with_users(session: AsyncSession):
    stmt = (
        select(Post).options(joinedload(Post.author)).order_by(Post.id)
        )
    result = await session.execute(stmt)
    return result.scalars().all()


async def get_users_with_posts(session: AsyncSession):
    stmt = (
        select(User).options(joinedload(User.posts)).order_by(User.id)
        )
    result = await session.execute(stmt)
    users = result.unique().scalars().all()
    for user in users:
        for post in user.posts:
            print(post)
    stmt = (
        select(User).options(selectinload(User.posts)).order_by(User.id)
        )
    result = await session.execute(stmt)
    return result.scalars().all()
