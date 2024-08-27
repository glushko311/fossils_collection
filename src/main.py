import uvicorn

from src.config import settings

from routers.user_router import user_router
from routers.main_router import main_router

from create_app import create_app


main_app = create_app(create_custom_static_urls=True)

main_app.include_router(main_router)
main_app.include_router(user_router)


if __name__ == "__main__":

    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
