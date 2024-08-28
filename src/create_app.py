import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.db_helper import db_helper

logger = logging.getLogger(__file__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    logger.info("Dispose DB engine")
    await db_helper.dispose()


def create_app(
) -> FastAPI:
    app = FastAPI(
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
    )
    return app
