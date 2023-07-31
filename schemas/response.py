from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    nickname: str


class IdeaResponse(BaseModel):
    id: int
    name: str
    description: str
    user_id: int


class IdeaCreate(BaseModel):
    id: int
    name: str
    description: str
    user_id: int