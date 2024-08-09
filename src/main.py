import os

from dotenv import load_dotenv


from fastapi import FastAPI
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


load_dotenv()
engine = create_async_engine(url=os.getenv("DATABASE_URL"), echo=True)
SessionLocal = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


app = FastAPI()


