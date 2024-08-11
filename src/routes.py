from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db_helper import db_helper
from models import User
from schemas import UserBase
from config import settings


router = APIRouter(prefix=settings.api_v1_prefix)


@router.get("/")
def main():
    return "Hello world"


@router.post("/users")
async def add_user(
    user: UserBase, db: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.get("/users")
async def get_users(db: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    results = await db.execute(select(User))
    users = results.scalars().all()
    return {"users": users}
