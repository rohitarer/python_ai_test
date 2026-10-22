from fastapi import FastAPI
from routers.tickets import router
from database import Base, engine
import db_models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)