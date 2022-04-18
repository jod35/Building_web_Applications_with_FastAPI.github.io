from fastapi import FastAPI, Query, Body
from typing import Optional


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/greet/{name}")
def greet_name(name: str):

    return {"name": f"Hello {name}"}


@app.get("/hey")
def greet_optional_name(name: str = Query(default="World", max_length=40)):

    return {"message": f"Hey {name}"}


@app.post("/users")
def create_a_user(username: str = Body(...), email: str = Body(...)):
    return {"username": username, "email": email}
