
# from dotenv import load_dotenv
from pydantic import BaseModel

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


engine = create_engine("sqlite:///db.sqlite3", connect_args={"check_same_thread":False}, echo=True)

SessionLocal = sessionmaker(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)


Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserBase(BaseModel):
    username: str


app = FastAPI()


@app.get("/")
def main():
    return "Hello world"


@app.post("/users")
def add_user(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {'users': users}
