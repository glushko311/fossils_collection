
# from dotenv import load_dotenv
from pydantic import BaseModel

from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", connect_args={"check_same_thread":False}, echo=True)

SessionLocal = async_sessionmaker(engine)

# Base = declarative_base()


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)


# Base.metadata.create_all(engine)


async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


class UserBase(BaseModel):
    username: str


app = FastAPI()


@app.get("/")
def main():
    return "Hello world"


@app.post("/users")
async def add_user(user: UserBase, db: AsyncSession = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(User))
    users = results.scalars().all()
    return {'users': users}

