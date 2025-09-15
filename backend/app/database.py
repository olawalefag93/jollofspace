import os
from dotenv import load_dotenv
from databases import Database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

# Load environment variables from .env
load_dotenv()

# Fetch the DB URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Async database connection
database = Database(DATABASE_URL)

# SQLAlchemy setup
metadata = MetaData()
Base = declarative_base()
