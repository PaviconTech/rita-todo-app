from sqlalchemy.orm import Session
import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo

def update_todo(db: Session, todo_id: int, updated: schemas.TodoCreate):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        todo.title = updated.title
        todo.completed = updated.completed
        db.commit()
        db.refresh(todo)
    return todo

