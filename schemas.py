from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    title: str
    description: str
    user_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    is_done: bool

    class Config:
        orm_mode = True
