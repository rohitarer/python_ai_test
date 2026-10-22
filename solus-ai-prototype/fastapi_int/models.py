from pydantic import BaseModel, Field

class Employee(BaseModel):
    name: str = Field(min_length = 2)
    id: int = Field(gt = 0)
    hours: float = Field(ge= 0, le= 24)


class EmployeeResponse(BaseModel):
    name: str
    id: int
    hours: float
