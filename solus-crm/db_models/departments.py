from sqlalchemy import Column, Integer, String
from database import Base

class DepartmentDB(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable= False)
