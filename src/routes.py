from fastapi import Depends, APIRouter

from database import get_db
from models import User
from schemas import UserBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


router = APIRouter()


@router.get("/")
def main():
    return "Hello world"


@router.post("/users")
async def add_user(user: UserBase, db: AsyncSession = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(User))
    users = results.scalars().all()
    return {"users": users}
