from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.async_engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.async_session = async_sessionmaker(
            self.async_engine,
            expire_on_commit=False,
            )

    async def get_session_dependency(self):
        async with self.async_session() as session:
            yield session


db_helper = DataBaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
    )
