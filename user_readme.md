# FastAPI CRUD with SQLAlchemy and SQLite

This project implements a basic CRUD (Create, Read, Update, Delete) API using FastAPI, SQLAlchemy, and SQLite. It provides endpoints to manipulate user data stored in an SQLite database.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the FastAPI application:
    ```bash
    uvicorn user_main:app --reload
    ```

## Usage
The API exposes the following endpoints:

* GET /users/{user_id}: Retrieve information about a specific user.
* POST /users/: Create a new user.
* PUT /users/{user_id}: Update information about an existing user.
* DELETE /users/{user_id}: Delete a user.

## License
This project is licensed under the MIT License.