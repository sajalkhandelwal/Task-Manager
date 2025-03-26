# Task Management API

A Django REST Framework-based API for task management.

## Features

- User authentication with JWT tokens
- Create and manage tasks
- Assign tasks to multiple users
- View tasks assigned to specific users
- Task status tracking

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

#### 1. Obtain JWT Token
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```
Response:
```json
{
    "access": "your.jwt.access.token"
}
```

#### 2. Refresh JWT Token
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "your.jwt.refresh.token"
  }'
```
Response:
```json
{
    "access": "your.new.jwt.access.token"
}
```

### Users

#### 1. Register a New User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "your_secure_password",
    "first_name": "John",
    "last_name": "Doe"
  }'
```
Response:
```json
{
    "id": 1,
    "username": "newuser",
    "email": "newuser@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### 2. Get User Details 
```bash
curl http://localhost:8000/api/users/1/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response:
```json
{
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### 3. Update User 
```bash
curl -X PUT http://localhost:8000/api/users/1/ \
  -H "Authorization: Bearer your.jwt.access.token" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "updated@example.com",
    "first_name": "Johnny",
    "last_name": "Doe"
  }'
```
Response:
```json
{
    "id": 1,
    "username": "user1",
    "email": "updated@example.com",
    "first_name": "Johnny",
    "last_name": "Doe"
}
```

#### 4. Delete User 
```bash
curl -X DELETE http://localhost:8000/api/users/1/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response: HTTP 204 No Content

### Tasks

#### 1. List All Tasks 
```bash
curl http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response:
```json
[
    {
        "id": 1,
        "name": "Complete project documentation",
        "description": "Write comprehensive documentation for the task management API",
        "task_type": "work",
        "status": "pending",
        "created_at": "2024-03-26T12:00:00Z",
        "updated_at": "2024-03-26T12:00:00Z",
        "completed_at": null,
        "assigned_to": [
            {
                "id": 1,
                "username": "user1",
                "email": "user1@example.com",
                "first_name": "John",
                "last_name": "Doe"
            }
        ],
        "created_by": {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        }
    }
]
```

#### 2. Create a New Task 
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer your.jwt.access.token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "work",
    "assigned_to_ids": [1, 2]
  }'
```
Response:
```json
{
    "id": 1,
    "name": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "work",
    "status": "pending",
    "created_at": "2024-03-26T12:00:00Z",
    "updated_at": "2024-03-26T12:00:00Z",
    "completed_at": null,
    "assigned_to": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        }
    ],
    "created_by": {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Jane",
        "last_name": "Smith"
    }
}
```

#### 3. Get Task Details 
```bash
curl http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response:
```json
{
    "id": 1,
    "name": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "work",
    "status": "pending",
    "created_at": "2024-03-26T12:00:00Z",
    "updated_at": "2024-03-26T12:00:00Z",
    "completed_at": null,
    "assigned_to": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe"
        }
    ],
    "created_by": {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Jane",
        "last_name": "Smith"
    }
}
```

#### 4. Update Task 
```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer your.jwt.access.token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated task name",
    "description": "Updated task description",
    "task_type": "work",
    "status": "in_progress",
    "assigned_to_ids": [1, 2, 3]
  }'
```
Response:
```json
{
    "id": 1,
    "name": "Updated task name",
    "description": "Updated task description",
    "task_type": "work",
    "status": "in_progress",
    "created_at": "2024-03-26T12:00:00Z",
    "updated_at": "2024-03-26T12:30:00Z",
    "completed_at": null,
    "assigned_to": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        },
        {
            "id": 3,
            "username": "user3",
            "email": "user3@example.com",
            "first_name": "Bob",
            "last_name": "Johnson"
        }
    ],
    "created_by": {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Jane",
        "last_name": "Smith"
    }
}
```

#### 5. Delete Task 
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response: HTTP 204 No Content

#### 6. Assign Users to a Task 
```bash
curl -X POST http://localhost:8000/api/tasks/1/assign_users/ \
  -H "Authorization: Bearer your.jwt.access.token" \
  -H "Content-Type: application/json" \
  -d '{
    "user_ids": [1, 2, 3]
  }'
```
Response:
```json
{
    "id": 1,
    "name": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "work",
    "status": "pending",
    "created_at": "2024-03-26T12:00:00Z",
    "updated_at": "2024-03-26T12:30:00Z",
    "completed_at": null,
    "assigned_to": [
        {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        },
        {
            "id": 3,
            "username": "user3",
            "email": "user3@example.com",
            "first_name": "Bob",
            "last_name": "Johnson"
        }
    ],
    "created_by": {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Jane",
        "last_name": "Smith"
    }
}
```

#### 7. Get User's Tasks 
```bash
curl http://localhost:8000/api/tasks/my_tasks/ \
  -H "Authorization: Bearer your.jwt.access.token"
```
Response:
```json
[
    {
        "id": 1,
        "name": "Complete project documentation",
        "description": "Write comprehensive documentation for the task management API",
        "task_type": "work",
        "status": "pending",
        "created_at": "2024-03-26T12:00:00Z",
        "updated_at": "2024-03-26T12:30:00Z",
        "completed_at": null,
        "assigned_to": [
            {
                "id": 1,
                "username": "user1",
                "email": "user1@example.com",
                "first_name": "John",
                "last_name": "Doe"
            }
        ],
        "created_by": {
            "id": 2,
            "username": "user2",
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        }
    }
]
```

## Authentication

The API uses JWT (JSON Web Token) authentication. To use the API:

1. Register a new user using the `/api/register/` endpoint
2. Obtain a token by sending a POST request to `/api/token/` with your username and password
3. Include the token in the Authorization header of subsequent requests
4. Use the token refresh endpoint to get a new token when the current one expires

## Models

### User
- id (auto-generated)
- username
- email
- first_name
- last_name
- created_at
- updated_at

### Task
- id (auto-generated)
- name
- description
- task_type (personal/work/shopping/other)
- status (pending/in_progress/completed)
- created_at
- updated_at
- completed_at
- assigned_to (many-to-many relationship with User)
- created_by (foreign key to User) 