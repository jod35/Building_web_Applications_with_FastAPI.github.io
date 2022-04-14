from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get('/greet/{name}')
def greet_name(name:str):
    
    return {"name":f"Hello {name}"}


@app.get("/hey")
def greet_optional_name(name:Optional[str]="World"):

    return {"message": f"Hey {name}"}

