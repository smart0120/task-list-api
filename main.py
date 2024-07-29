from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)

Base.metadata.create_all(bind=engine)

class TaskCreate(BaseModel):
    task: str

class TaskResponse(TaskCreate):
    id: int

@app.get("/api/tasks", response_model=List[TaskResponse])
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return tasks

@app.post("/api/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(task=task.task)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()
    return db_task
