from fastapi import FastAPI, HTTPException

from db import session
from models.todo import Todo

app = FastAPI()


@app.post("/")
async def create_todo(text: str, is_done: bool = False):
    todo = Todo(text=text, is_done=is_done)
    session.add(todo)
    session.commit()
    return { "todo added": todo.text }

@app.get("/{id}")
async def get_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/{id}")
async def update_todo(id: int, new_text: str, is_done: bool):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if new_text:
        todo.text = new_text
    todo.is_done = is_done
    session.add(todo)
    session.commit()
    return {"message": "Task updated"}

@app.delete("/{id}")
async def delete_todo(id: int):
    todo_query = session.query(Todo).filter(Todo.id == id)
    todo = todo_query.first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    session.delete(todo)
    session.commit()
    return { "message": f"Task {id} deleted successfully" }
