from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./uni.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    average = Column(Float)
    graduated = Column(Boolean)
    courses = relationship("Course", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    unit = Column(Integer)
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="courses")

Base.metadata.create_all(bind=engine)

# CRUD operations for students
@app.post("/students/")
def create_student(firstname: str, lastname: str, average: float, graduated: bool):
    db = SessionLocal()
    student = Student(firstname=firstname, lastname=lastname, average=average, graduated=graduated)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students/{student_id}")
def read_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/")
def read_students():
    db = SessionLocal()
    students = db.query(Student).all()
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, firstname: str, lastname: str, average: float, graduated: bool):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    student.firstname = firstname
    student.lastname = lastname
    student.average = average
    student.graduated = graduated
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    db = SessionLocal()
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

# CRUD operations for courses
@app.post("/courses/")
def create_course(name: str, unit: int, student_id: int):
    db = SessionLocal()
    course = Course(name=name, unit=unit, student_id=student_id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@app.get("/courses/")
def read_courses():
    db = SessionLocal()
    courses = db.query(Course).all()
    return courses


@app.get("/courses/{course_id}")
def read_course(course_id: int):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{course_id}")
def update_course(course_id: int, name: str, unit: int):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    course.name = name
    course.unit = unit
    db.commit()
    db.refresh(course)
    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}
