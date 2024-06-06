from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base

if TYPE_CHECKING:
    from core.models.user import User


class Post(Base):
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
        )
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(" \
               f"id={self.id}," \
               f"title={self.title!r}," \
               f" author_id={self.author_id!r})"

    def __repr__(self) -> str:
        return str(self)
