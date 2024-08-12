from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db_helper import db_helper
from models.user import User
from schemas.user_schema import UserBase
from config import settings


user_router = APIRouter(prefix=settings.api_v1_prefix + "/users")


@user_router.post("/")
async def add_user(
    user: UserBase, db: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@user_router.get("/")
async def get_users(db: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    results = await db.execute(select(User))
    users = results.scalars().all()
    return {"users": users}
