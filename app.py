import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from models import User, Idea
from schemas.response import UserResponse, IdeaResponse
from schemas.response import IdeaCreate



app = FastAPI()


@app.get('/users/', response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.get("/users/{user_id}/ideas/", response_model=List[IdeaResponse])
def get_ideas_by_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404)
    return user.ideas
@app.post("/ideas")
def create_idea(idea: IdeaCreate, db: Session = Depends(get_db)):
    db_idea = Idea(name=idea.name, description=idea.description)
    db.add(db_idea)
    db.commit()
    db.refresh(db_idea)
    return {'message": "Idea created successfully'}



if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8002)
