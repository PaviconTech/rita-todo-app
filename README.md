RITA TODO APP
- A simple and functional Todo API built using FastAPI, SQLAlchemy, and SQLite for task management.
PROJECT STRUCTURE
rita-todo-app/

 backend/
 main.py           # Entry point for the FastAPI app
 models.py         # SQLAlchemy models (database tables)
 schemas.py        # Pydantic schemas (request/response validation)
 database.py       # Database configuration and session management
 crud.py           # Functions for interacting with the database (CRUD)
 requirements.txt  # List of required Python packages
 README.md         # Documentation
backend/
MAIN.PY– Application Entry Point
Initializes the FastAPI application.
Defines API routes (e.g., create, read, update, delete todos).
Runs the app using Uvicorn.

MODELS.PY – SQLAlchemy Models
Defines the structure of database tables using SQLAlchemy.
Each class in this file corresponds to a table in the database.
Example: Todo table with fields like id, title, description, and completed.

SCHEMAS.PY – Pydantic Schemas
Provides request and response validation using Pydantic.
Ensures only properly formatted data is accepted and returned by the API.
Defines schemas like TodoCreate, TodoUpdate, and TodoResponse.

DATABASE.PY – Database Configuration
Sets up the connection to the SQLite database using SQLAlchemy.
Includes engine creation, session configuration, and Base class.
Used to initialize and connect to the database.

CRUD.PY– CRUD Operations
Contains functions for Create, Read, Update, and Delete operations on todos.
Called inside the route handlers to interact with the database in a clean way.

REQUIREMENTS.TXT – Dependencies
Lists all Python packages required to run the backend.

