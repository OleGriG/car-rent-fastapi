import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")
    FIXED_SALT_FOR_HESH: str = os.getenv("FIXED_SALT_FOR_HESH", '')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
