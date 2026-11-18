from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


# Add the POST, GET-by-id, PUT, and DELETE routes described in README.md.