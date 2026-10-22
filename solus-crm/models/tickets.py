from pydantic import BaseModel, Field
from typing import Literal

class TicketCreate(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=3)
    desc: str = Field(min_length=5)
    dept_id: int = Field(gt=0)
    status: Literal['open', 'in_progress', 'resolved'] = 'open'


class TicketAssign(BaseModel):
    employee_id: int = Field(gt=0)