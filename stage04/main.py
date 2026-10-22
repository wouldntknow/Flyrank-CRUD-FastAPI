from asyncio import Task

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Tasks(BaseModel):
    id: int
    title:str
    status:bool

a=[
    Tasks(id=1, title="Task 1", status=True),
    Tasks(id=2, title="Task 2", status=False),
    Tasks(id=3, title="Task 3", status=True)
]


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return { "tasks": a }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in a:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task_title: str):
    if task_title == "":
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    else:
        task = Tasks(id=len(a) + 1, title=task_title, status=False)
        a.append(task)
        return task
    
@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_title: str,
    task_status: bool
):
    # Find the EXISTING task
    for task in a:
        if task_id==task.id:

            # Update the existing task
            task.title = task_title
            task.status = task_status
            
            return task

    # ID doesn't exist
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in a:
        if task_id == task.id:
            a.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
