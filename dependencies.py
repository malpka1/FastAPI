import os
from dotenv import load_dotenv
from fastapi import Depends, requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from services.user import UserService

load_dotenv()
SQL_URL = os.environ.get("SQL_URL")
engine = create_engine(SQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
response = requests.get('https://www.boredapi.com/api/activity')
data = response.json()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_group_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db=db)