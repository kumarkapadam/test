from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import uvicorn

from app import crud, models, schemas
from app.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return "welcome to TO_Do_APP"


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Route to get all the todo's, it has 2 query params, a skip and a limit
@app.get("/")
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos


# Route to create a new todo, it requires a todo in request body
@app.post("/")
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return db_todo


# Route to change the done named bool
@app.put("/{id}")
def update_todo(id: int, done: bool = True, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id=id, done=done)
    return db_todo


if __name__ == "__main__":
    uvicorn.run(app)
