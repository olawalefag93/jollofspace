from fastapi import FastAPI
from sqlalchemy import create_engine
from app import database, models, routes
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# add this route for "/" requests
@app.get("/")
def root():
    return {"message": "Welcome to the Jollofspace API!"}

# Include API routes
app.include_router(routes.router)

# Start DB connection and create tables
@app.on_event("startup")
async def startup():
    engine = create_engine(os.getenv("DATABASE_URL"))
    models.Base.metadata.create_all(bind=engine)
    await database.database.connect()

# Disconnect DB on shutdown
@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()

