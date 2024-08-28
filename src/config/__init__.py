from pydantic_settings import BaseSettings

from src.config.config import (
    app_env,
    ProductionSettings,
    TestingSettings,
    DevelopmentSettings,
)


if app_env == "production":
    settings: BaseSettings = ProductionSettings()
elif app_env == "testing":
    settings: BaseSettings = TestingSettings()
else:
    settings: BaseSettings = DevelopmentSettings()
