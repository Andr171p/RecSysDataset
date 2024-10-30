'''from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class AccessDatabaseURL(BaseSettings):
    PUBLIC_URL: PostgresDsn = 'postgresql+asyncpg://postgres:oklNXvawdATGqbEvjIxprKTNRWrWEHSn@monorail.proxy.rlwy.net:16488/railway'
'''


class AccessDatabaseURL:
    PUBLIC_URL: str = 'postgresql+asyncpg://postgres:oklNXvawdATGqbEvjIxprKTNRWrWEHSn@monorail.proxy.rlwy.net:16488/railway'
