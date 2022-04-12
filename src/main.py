from fastapi import FastAPI
from typing import Optional


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get('/{name}')
def greet_name(name:str):
    
    return {"name":f"Hello {name}"}


@app.get("/greet")
def greet_otional_name(name:Optional[str]="World"):

    return {"message": f"Helo {name}"}

