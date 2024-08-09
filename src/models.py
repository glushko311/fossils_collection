from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self):
        return f"User {self.username}, created_at={self.date_created}"
