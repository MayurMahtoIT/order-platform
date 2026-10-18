from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All configuration comes from environment variables (12-factor app)."""

    database_url: str = "postgresql+psycopg://orders:orders_dev_pw@localhost:5433/orders"
    service_name: str = "order-service"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
