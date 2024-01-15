# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from typing import List
from database.database import (
    get_db,
    list_users as db_list_users,  # Змінено ім'я тут
    create_user,
    create_user_task,
    list_tasks,
    create_task,
    read_task,
    update_task,
    list_user_tasks,
    delete_task,
)
from schemas.schemas import UserCreate, User as UserSchema, TaskCreate, Task as TaskSchema

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def read_root():
    return {"message": "Hello, this is the root path!"}

@app.get("/users/", response_model=List[UserSchema])
def list_users(db: Session = Depends(get_db)):
    return db_list_users(db)  # Змінено виклик функції тут

# Інші ручки...

@app.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)

@app.post("/users/{user_id}/tasks/", response_model=TaskSchema)
def create_user_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return create_user_task(user_id, task, db)

@app.get("/tasks/", response_model=List[TaskSchema])
def list_tasks(db: Session = Depends(get_db)):
    return list_tasks(db)

@app.post("/tasks/", response_model=TaskSchema)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(task, db)

@app.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return read_task(task_id, db)

@app.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return update_task(task_id, task, db)

@app.get("/users/{user_id}/tasks/", response_model=List[TaskSchema])
def list_user_tasks(user_id: int, db: Session = Depends(get_db)):
    return list_user_tasks(user_id, db)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task(task_id, db)
