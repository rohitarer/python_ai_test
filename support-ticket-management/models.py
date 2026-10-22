from pydantic import BaseModel, Field
from typing import Literal, Optional

class Ticket(BaseModel):
    id: int = Field(gt = 0)
    title: str = Field(min_length = 3)
    description: str = Field(min_length = 5)
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "in_progress", "closed"]
    assigned_user_id: int = Field(gt = 0)



class TicketResponse(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "in_progress", "closed"]
    assigned_user_id: int


class TicketUpdate(BaseModel):
    priority: Optional[Literal["low", "medium", "high"]] = None
    status: Optional[Literal["open", "in_progress", "closed"]] = None