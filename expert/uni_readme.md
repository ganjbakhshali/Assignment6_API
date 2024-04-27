# University System with FastAPI, SQLAlchemy, and PostgreSQL

This project implements a simple university system using FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on both students and courses.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Start PostgreSQL Docker container::
    ```bash
    docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=ramze_akbar_agha -e POSTGRES_USER=akbar -e POSTGRES_DB=database_akbar -d postgres
    ```
4. Update database connection URL:

    Modify the SQLALCHEMY_DATABASE_URL variable in the code (main.py) to reflect your PostgreSQL connection string.

5. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```



## Usage
The API exposes the following endpoints:

Students
* GET /students/: Retrieve all students.
* GET /students/{student_id}: Retrieve information about a specific student.
* POST /students/: Create a new student.
* PUT /students/{student_id}: Update information about an existing student.
* DELETE /students/{student_id}: Delete a student.

Courses
* POST /courses/: Create a new course.
* PUT /courses/{course_id}: Update information about an existing course.
* DELETE /courses/{course_id}: Delete a course.
* GET /courses/: Retrieve all courses.

## License
This project is licensed under the MIT License.