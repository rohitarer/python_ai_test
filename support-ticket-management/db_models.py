from sqlalchemy import Column, Integer, String
from database import Base

class TicketsDB(Base):
    __tablename__ = "tickets"

    id= Column(Integer, primary_key= True, index= True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    priority = Column(String, nullable = False)
    status = Column(String, nullable = False)
    assigned_user_id = Column(Integer, nullable = False)