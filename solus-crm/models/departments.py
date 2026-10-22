from pydantic import BaseModel, Field

class createDepartment(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2)