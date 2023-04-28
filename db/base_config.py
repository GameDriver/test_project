from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///my_database.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

