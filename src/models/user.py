from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.int_id_mixin import IntIdPkMixin


class User(IntIdPkMixin, Base):

    username: Mapped[str] = mapped_column(String(32), unique=True)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"User {self.username}, created_at={self.date_created}"
