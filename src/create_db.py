from models.base import Base
from db_helper import db_helper

import asyncio


async def create_db():
    """
    One time script - coroutine responsible for creating database tables
    """
    async with db_helper.engine.begin() as conn:
        from models.user import User

        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await db_helper.engine.dispose()


asyncio.run(create_db())
