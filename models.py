from sqlmodel import  SQLModel, Field

class Student(SQLModel, table=True):
    reg_id: int = Field(default=None, primary_key=True)
    surname: str
    first_name: str
    gender: str
    address: str
    passport: str
    
    
    
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
        "example": {
            "surname": "Nwokoro",
            "first_name": "Oluoma",
            "gender": "male",
            "address": "Ihiala, Anambra",
            "passport": "https://linktomyimage.com/image.png"
            
        }
    }


class StudentUpdate(SQLModel):
    surname: str
    first_name: str
    gender: str
    address: str
    passport: str
    
    
    
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
        "example": {
            "surname": "Nwokoro",
            "first_name": "Oluoma",
            "gender": "male",
            "address": "Ihiala, Anambra",
            "passport": "https://linktomyimage.com/image.png"
            
        }
    }
