from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = "sqlite:///./crm.db"  #local file DB

engine = create_engine(  #DB engine
    DATABASE_URL,
    connect_args={"check_same_thread": False},  #for SQLite + FastAPI
)

SessionLocal = sessionmaker(  #create db session factory
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def init_db() -> None:
    Base.metadata.create_all(bind=engine)  #create tables if missing

def get_db():
    db = SessionLocal()  #open session
    try:
        yield db  #session to route
    finally:
        db.close()  #close session
