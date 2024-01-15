#pip install fastapi uvicorn sqlalchemy
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User, Task, SessionLocal, engine
from schemas import UserCreate, User as UserSchema, TaskCreate, Task as TaskSchema
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI()

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

@app.get("/", response_class=JSONResponse)
def read_root():
    return {"message": "Привіт, це кореневий шлях!"}

@app.get("/users/", response_model=List[UserSchema])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Create a new user
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/users/{user_id}/tasks/", response_model=TaskSchema)
def create_user_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    # Find a user by their ID
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Remove user_id from task.dict()
    task_data = task.dict(exclude={"user_id"})

    # Створіть нове завдання для користувача
    db_task = Task(**task_data, user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[TaskSchema])
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@app.post("/tasks/", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    # Create a new task
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task



@app.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)):
    # Getting information about a specific task
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# Changes in update_task arguments
@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    # Updating information about a specific task
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description
    db_task.is_done = task.is_done

    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/users/{user_id}/tasks/", response_model=List[TaskSchema])
def list_user_tasks(user_id: int, db: Session = Depends(get_db)):
    # We get all tasks for a specific user
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted successfully"}

