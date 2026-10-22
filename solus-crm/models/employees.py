from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=3)
    dept_id: int = Field(gt=0)