# Task Management API

A Django REST Framework-based API for managing tasks and assignments.

## Features

- User authentication with JWT tokens
- Create and manage tasks
- Assign tasks to multiple users
- View tasks assigned to specific users
- Task status tracking
- Task categorization

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
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Users
- `POST /api/register/` - Register a new user
- `GET /api/users/{id}/` - Get user details (requires authentication)
- `PUT /api/users/{id}/` - Update user (requires authentication)
- `DELETE /api/users/{id}/` - Delete user (requires authentication)

### Tasks
- `GET /api/tasks/` - List all tasks (assigned to or created by the user)
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task
- `POST /api/tasks/{id}/assign_users/` - Assign users to a task
- `GET /api/tasks/my_tasks/` - Get tasks assigned to the current user

## API Request Examples

### Register a New User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "your_secure_password",
    "mobile": "1234567890",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

### Create a Task
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Complete project documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "work",
    "assigned_to_ids": [1, 2]
  }'
```

### Assign Users to a Task
```bash
curl -X POST http://localhost:8000/api/tasks/1/assign_users/ \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "user_ids": [1, 2, 3]
  }'
```

### Get User's Tasks
```bash
curl http://localhost:8000/api/tasks/my_tasks/ \
  -H "Authorization: Bearer <your_token>"
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