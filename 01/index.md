# 01- Introduction to FastAPI

## What is FastAPI?

FastAPI is a web framework written in Python that is specifc to building web APIs. FastAPI gives a very easy to develop REST as well as GraphQL APIs.In this module I introduce FastAPI and we look at what you need to know to get started. FastAPI allows you to use features of modern Python features to build web APIs.

To build a FastAPI application you will start by creating a virtual environment with

```
$ python3 -m venv env
```

Go ahead and activate the virtual environment

On Linux / MacOS

```
$ source env/bin/activate
```

On Windows (CMD)

```
$ env\Scripts\activate.bat
```

Within our virtual environment, then we proceed to installing FastAPI with the `pip` package manager

```
(env) $ pip install fastapi
```

At this point, shall have the following folder structure

```
├── env
└── main.py
```

`main.py` will be our main application file. Ok, let us build our first FastAPI application. In main.py, go ahead and add the following code.

```
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}
```

This code alone has helped us to build our first FastAPI application. What has happened?

We begun by importing the FastAPI class
