from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import select
from connection import get_session
from models import Student, StudentUpdate

student_router = APIRouter(tags=["Student"])


""" This route create registers new student"""
@student_router.post("/register")
async def create_student(new_student: Student,session=Depends(get_session)):
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    return {
    "message": "Student created successfully"    }
    

""" This endpoint retrieves student details"""
@student_router.get("/", response_model=List[Student], status_code = status.HTTP_200_OK)
async def retrieve_all_students(session=Depends(get_session)):
    statement = select(Student)
    students = session.exec(statement).all()
    return students
        
    
@student_router.get("/{reg_id}", response_model=Student, status_code = status.HTTP_200_OK)
async def retrieve_single_student(reg_id: int, session=Depends(get_session)):
    student = session.get(Student, reg_id)
    if student:
        return student
    raise HTTPException(  status_code=status.HTTP_404_NOT_FOUND,detail=f"Student with Registration ID {reg_id} does not exist")

    
""" This endpoint updates student details"""
@student_router.put("/edit/{reg_id}", response_model= Student, status_code = status.HTTP_202_ACCEPTED)
async def update_student(reg_id: int, new_data: StudentUpdate, session= Depends(get_session)):
    student = session.get(Student, reg_id)
    if student: 
        student_data = new_data.dict(exclude_unset=True)
        for key, value in student_data.items():
            setattr(student, key, value)
        session.add(student)
        session.commit()
        session.refresh(student)
        
        return student
    raise HTTPException(  status_code=status.HTTP_404_NOT_FOUND,detail=f"Student with Registration ID {reg_id} does not exist")

""" This endpoint delets student details"""
@student_router.delete("/delete/{reg_id}")
async def delete_student(reg_id: int, session=Depends(get_session)):
    student = session.get(Student, reg_id)
    if student:
        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}
    raise HTTPException(  status_code=status.HTTP_404_NOT_FOUND,detail=f"Student with Registration ID {reg_id} does not exist")
        
        
