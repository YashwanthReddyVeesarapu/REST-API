from pydantic import BaseSettings


class Settings(BaseSettings):
    salt: str
    key: str
    