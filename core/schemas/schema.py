from pydantic import BaseModel

class Task(BaseModel):
    task_id: int
    task_name: str

class User(BaseModel):
    username: str
    email: str
