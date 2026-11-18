import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_PATH = Path(__file__).with_name("tasks.db")

app = FastAPI(title="Persistent Task API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database() -> None:
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


def row_to_task(row: sqlite3.Row) -> Task:
    return Task(
        id=row["id"],
        title=row["title"],
        completed=bool(row["completed"]),
    )


initialize_database()


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    raise NotImplementedError