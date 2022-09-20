from fastapi import FastAPI
from fastapi_offline import FastAPIOffline
from connection import conn
from routes import student_router

import uvicorn


# app = FastAPIOffline()


app = FastAPI(
    title="Nwokoro", description="This is my student registration assignment")



# Register routes
app.include_router(student_router, prefix="/student")

# connection starting
@app.on_event("startup")
def on_startup():
    conn()
    

# Home page 
@app.get("/")
async def root():    
    return {
        "Name": "Nwokoro V Oluoma",
        "Department": "Computer Science",
        "Course Title": "Introduction to Computer Science",
        "Course Code": "123",
        "Lecturer Name": "Dr. Python", 
        "Assignment link": "https://nwokoro.deta.dev/docs"
    }
    
    
    

if __name__ == '__main__':
 uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)