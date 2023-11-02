from fastapi import FastAPI
from core.schemas.schema import Task, User

app = FastAPI()

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    task = {"task_id": task_id, "task_name": "Ejemplo de artículo"}
    return task

@app.post("/users/", response_model=User)
async def create_user(user: User):
    return user
