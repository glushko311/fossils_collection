from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from config import settings

from routes import router
from src.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print("dispose engine")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
