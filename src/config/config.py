import os
from dotenv import load_dotenv

from pydantic import BaseModel
from pydantic_settings import BaseSettings


app_env: str = os.getenv("APP_ENV", "development")

if app_env == "production":
    env_file_name = "production.env"
elif app_env == "testing":
    env_file_name = "testing.env"
else:
    env_file_name = "develop.env"

env_path: str = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "src",
    "config",
    env_file_name,
)
load_dotenv(dotenv_path=env_path)


class DbSettings(BaseModel):
    url: str = (
        f"postgresql+asyncpg://"
        f"{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )
    # echo: bool = False
    echo: bool = True


class ConfigRun(BaseModel):
    host: str = os.getenv("APP_HOST")
    port: int = int(os.getenv("APP_PORT"))
    auto_reload: bool = bool(int(os.getenv("AUTO_RELOAD")))


class TestingSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()
    run: ConfigRun = ConfigRun()


class ProductionSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()
    db.echo = False
    run: ConfigRun = ConfigRun()


class DevelopmentSettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()
    run: ConfigRun = ConfigRun()
