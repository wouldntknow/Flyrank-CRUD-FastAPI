# Task Management API

A simple REST API built with **FastAPI** for creating, reading, updating, and deleting tasks.

## Features

- Health check endpoint
- Create tasks
- Get all tasks
- Get a single task by ID
- Update a task
- Delete a task
- Automatic interactive API documentation with Swagger UI

## Requirements

- Python 3.10+
- pip

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

## Running the API

Start the development server with:

```bash
uvicorn main:app --reload
```

> Replace `main` with the name of your Python file if it is different. For example, if your file is `app.py`, use `uvicorn app:app --reload`.

The API will be available at:

```text
http://127.0.0.1:8000
```

## Interactive API Documentation

FastAPI automatically provides interactive documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test all endpoints directly from your browser.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## Health Check

### `GET /health`

Checks whether the API is running.

### Response

```json
{
  "status": "ok"
}
```

---

## Get All Tasks

### `GET /tasks`

Returns all tasks.

### Example response

```json
{
  "tasks": [
    {
      "task_id": 1,
      "task_title": "Task 1",
      "task_status": true
    },
    {
      "task_id": 2,
      "task_title": "Task 2",
      "task_status": false
    }
  ]
}
```

---

## Get a Single Task

### `GET /tasks/{task_id}`

Returns a task using its ID.

### Example

```text
GET /tasks/1
```

### Response

```json
{
  "task_id": 1,
  "task_title": "Task 1",
  "task_status": true
}
```

If the task does not exist, the API returns:

```json
{
  "detail": "Task not found"
}
```

with HTTP status `404`.

---

## Create a Task

### `POST /tasks`

Creates a new task.

The task title is passed as a query parameter.

### Example

```text
POST /tasks?task_title=Learn%20FastAPI
```

### Response

```json
{
  "task_id": 4,
  "task_title": "Learn FastAPI",
  "task_status": false
}
```

New tasks are created with `task_status` set to `false`.

---

## Update a Task

### `PUT /tasks/{task_id}`

Updates an existing task.

The task ID is provided in the URL.

The new title and status are provided as query parameters.

### Example

```text
PUT /tasks/1?task_title=Learn%20FastAPI&task_status=true
```

### Response

```json
{
  "task_id": 1,
  "task_title": "Learn FastAPI",
  "task_status": true
}
```

If the task does not exist:

```json
{
  "detail": "Task not found"
}
```

with HTTP status `404`.

---

## Delete a Task

### `DELETE /tasks/{task_id}`

Deletes a task using its ID.

### Example

```text
DELETE /tasks/1
```

### Response

```json
{
  "message": "Task deleted successfully"
}
```

If the task does not exist, the API returns a `404` error.

---

# Example Workflow

You can test the API in this order:

### 1. Check the API

```text
GET /health
```

### 2. View existing tasks

```text
GET /tasks
```

### 3. Create a task

```text
POST /tasks?task_title=Learn%20FastAPI
```

### 4. Get the new task

```text
GET /tasks/4
```

### 5. Update the task

```text
PUT /tasks/4?task_title=Build%20an%20API&task_status=true
```

### 6. View all tasks

```text
GET /tasks
```

### 7. Delete the task

```text
DELETE /tasks/4
```

---

# Project Structure

A simple project structure can look like:

```text
project/
│
├── main.py
├── README.md
├── .gitignore
└── .venv/
```

The `.venv` directory should not be committed to Git.

Example `.gitignore`:

```gitignore
.venv/
__pycache__/
*.pyc
.env
```

---

# Important Note About Data Storage

This API currently stores tasks in a **Python list in memory**.

For example:

```python
a = [
    Tasks(task_id=1, task_title="Task 1", task_status=True),
    Tasks(task_id=2, task_title="Task 2", task_status=False)
]
```

Because there is no database yet:

- Data is lost when the server restarts.
- Data is not persistent.
- The API is intended for learning/development purposes.

For a production application, the API should use a database such as PostgreSQL or SQLite.

---

# Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

## License

This project is available for learning and development purposes.