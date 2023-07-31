from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    nickname: str


class UserCreate(UserBase):
    pass