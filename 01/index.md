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

### What has happened?
We begin by importing the `FastAPI` class from the `fastapi` package. This helps us to create the main instance of our application. This instance allows us to create URLs which lead to different parts of our application.

`@app.get('/')` describes which HTTP method we shall use while accessing the `/` URL of our application. For this case, we are calling the `GET` HTTP method. This means that we can as well call other HTTP methods like 
- `POST` with  `@app.post` 
- `PUT` with  `@app.put`
- `PATCH` with  `@app.patch`
- `DELETE` with  `@app.delete`

on a URL such as `/`. 

We create a function cAnother step we shall make is to add our dependencies to a `requirements.txt` file so that we keep track of the versions of our packages. Do that with:
```
(env)$ pip freeze > requirements.txt
```

This is going to update our folder structure to alled `index` that will handle a request for the `/` URL. This returns a JSON message of `Hello World`.

Now let us run our application. To run it, we shall install `uvicorn` which is an ASGI server that will help our application to run asynchronously.

In your command prompt ot terminal, type the following command

```
(env)$ pip install uvicorn
```

Another step we shall make is to add our dependencies to a `requirements.txt` file so that we keep track of the versions of our packages. Do that with:


```
(env)$ pip freeze > requirements.txt
```

This is going to update our folder structure to 
