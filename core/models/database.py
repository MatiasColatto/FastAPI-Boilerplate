# core/models/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from decouple import config

databaseUrl = os.getenv("DATABASE_URL", config('DATABASE_URL', default='sqlite:///./test.db'))

engine = create_engine(databaseUrl)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
