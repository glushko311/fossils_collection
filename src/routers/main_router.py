from fastapi import APIRouter

from config import settings


main_router = APIRouter(prefix=settings.api_v1_prefix)


@main_router.get("/")
def main():
    return "Hello world"
