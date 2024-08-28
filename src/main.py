import logging

import uvicorn

from src.config import settings, app_env

from routers.user_router import user_router
from routers.main_router import main_router
from create_app import create_app
from src.logger.logger import setup_logger


setup_logger()
main_app = create_app()

main_app.include_router(main_router)
main_app.include_router(user_router)


if __name__ == "__main__":
    logger = logging.getLogger(__file__)
    # from src.logger.logger import logger
    # logger.name = __file__
    if app_env=="development":
        logger.info("Run into DEVELOPMENT environment")
        logger.info("Server autoreload = %s", settings.run.auto_reload)
        logger.info("To run swagger docs use http://0.0.0.0:8080/docs (Press CTRL+C to quit)")
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=settings.run.auto_reload,
    )
