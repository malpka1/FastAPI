from models import User
from schemas.inputs import UserCreate


class UserService:

    def __init__(self, db):
        self.__db = db

    def create_user(self, group: UserCreate):
        group_db = User(name=user.name, nickname=user.nickname)
        self.__db.add(user_db)
        self.__db.commit()
        self.__db.refresh(user_db)
        return user_db