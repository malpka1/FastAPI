from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    nickname = Column(String(20), nullable=False)

    ideas = relationship('Idea', backref='group', lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"


class Idea(Base):
    __tablename__ = 'idea'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return f"<Idea {self.name} {self.description}>"

