from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def root():
    return "Hallo Welt"

models.Base.metadata.create_all(engine)