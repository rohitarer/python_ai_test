from fastapi import FastAPI, HTTPException
from routers.departments import router as departmentRouter
from routers.employees import router as employeeRouter
from routers.tickets import router as ticketRouter

from database import Base, engine
import db_models.departments

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(departmentRouter)
app.include_router(employeeRouter)
app.include_router(ticketRouter)


@app.get("/health")
def health_check():
    return {
        'status': 'running',
        'security': 'solus crm'
    }


