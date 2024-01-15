from sqlalchemy.orm import Session
from models import User, Task, SessionLocal, engine
from schemas import UserCreate, User as UserSchema, TaskCreate, Task as TaskSchema
from typing import List
from fastapi import HTTPException, Depends

# Creating tables in the database at startup
User.metadata.create_all(bind=engine)
Task.metadata.create_all(bind=engine)

# A function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def list_users(db: Session = Depends(get_db)) -> List[UserSchema]:
    users = db.query(User).all()
    return users

def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserSchema:
    # Create a new user
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)) -> TaskSchema:
    # Find a user by their ID
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Remove user_id from task.dict()
    task_data = task.dict(exclude={"user_id"})

    # Create a new task for the user
    db_task = Task(**task_data, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def list_tasks(db: Session = Depends(get_db)) -> List[TaskSchema]:
    tasks = db.query(Task).all()
    return tasks

def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> TaskSchema:
    # Create a new task
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_task(task_id: int, db: Session = Depends(get_db)) -> TaskSchema:
    # Getting information about a specific task
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

from sqlalchemy import update

def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)) -> TaskSchema:
    # Updating information about a specific task
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # Create a dictionary with non-None values from TaskCreate
    task_data = task.dict(exclude_none=True)

    # Use the update statement to update the fields in the database
    db.execute(update(Task).where(Task.id == task_id).values(**task_data))
    db.commit()
    db.refresh(db_task)

    return db_task


def list_user_tasks(user_id: int, db: Session = Depends(get_db)) -> List[TaskSchema]:
    # We get all tasks for a specific user
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks

def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}
