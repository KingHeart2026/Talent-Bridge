from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.config import settings

#create database engine
engine = create_engine(
    settings.DATABASE_URL,     #this manages communication between your python appication and postgreSQL
    pool_pre_ping=True         #this checks that your connection is still usable before SQLAlchemy gives it to your application
)

#Create database session
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False
)

#Database dependency
class Base(DeclarativeBase):
    pass

#Database dependency
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()