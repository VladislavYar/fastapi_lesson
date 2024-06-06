import uuid

from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


def generate_token():
    return str(uuid.uuid4())


class AccessPermisson(Base):
    __table_args__ = (
        Index(
            "ix_unique_action_for_token",
            "token",
            "action",
            unique=True,
        ),
    )
    token: Mapped[str] = mapped_column(
        default=generate_token,
    )
    action: Mapped[str]
