from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
class student(BaseModel):
    name: str
    email: str
    age: int
    roll_number: str
    department: str

class studentResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    roll_number: str
    department: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student_logic(student: student):
    return student

def read_student_logic(id: int):
    # This is a placeholder logic, normally you'd fetch from DB
    return {"id": id, "name": "placeholder", "email": "placeholder", "age": 0, "roll_number": "0", "department": "placeholder"}

def update_student_logic(id: int, student: student):
    return studentResponse(id=id, **student.dict())

def delete_student_logic(id: int):
    return {"id": id, "message": "deleted"}

@app.post("/students")
def create_student_endpoint(student: student):
    return create_student_logic(student)

@app.get("/students/{id}")
def read_student_endpoint(id: int):
    return read_student_logic(id)

@app.put("/students/{id}")
def update_student_endpoint(id: int, student: student):
    return update_student_logic(id, student)

@app.delete("/students/{id}")
def delete_student_endpoint(id: int):
    return delete_student_logic(id)







