from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import settings

from src.base import Base

engine = create_async_engine(url=settings.db.url, echo=True)
SessionLocal = async_sessionmaker(engine)




async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
