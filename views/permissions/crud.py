from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.functions import count

from core.models import AccessPermisson


async def check_permission(
        session: AsyncSession,
        token: str,
        action: str,
) -> bool:
    stmt = (
        select(count(AccessPermisson.id))
        .where(
            AccessPermisson.token == token,
            AccessPermisson.action == action,
        )
        .limit(1)
    )
    total = await session.scalar(stmt)
    return bool(total)
