from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length = 2)
    email: EmailStr