from database import SessionLocal
from db_models.departments import DepartmentDB

db = SessionLocal()

deparment = DepartmentDB(id=1, name="Development")

db.add(deparment)
db.commit()

db.close()