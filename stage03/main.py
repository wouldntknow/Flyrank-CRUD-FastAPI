from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
class Tasks(BaseModel):
    id: int
    title: str
    status: bool

# create list of objects
a = [
    Tasks(id=1, title="Task 1", status=True),
    Tasks(id=2, title="Task 2", status=False),
    Tasks(id=3, title="Task 3", status=True)
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return { "tasks": a }
#     return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in a:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/create tasks")
def create_task(task_title: str):
    if task_title == "":
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    else:
        task = Tasks(id=len(a) + 1, title=task_title, status=False)
        a.append(task)
        return task
        


    