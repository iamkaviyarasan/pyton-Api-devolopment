# Old import statement
# from pydantic import BaseSettings

# New import statement
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"
        # env_file_encoding = "utf-8"
        # env_file_encoding = "utf-8"
        # env_file_encoding = "utf-8"

settings = Settings()
