# Managing Pydantic models with FastAPI

In the previous post, we looked at how we could require to provide the request body by using the `Body` function. We looked at how this can give us verbose request handler functions. In this case, we create Pydantic models to help us do our validations.

## What is Pydantic?

[Pydantic](https://pydantic-docs.helpmanual.io/) is the underlying data validation library used in FastAPI. It is a handy data parsing and validation library. It uses type hints to convert input types to the defined type, collects all errors with ValidationError, and is properly documented, making it easy to find.

## Creating Models

Using Pydantic, we can primarily describe our data as `models`. These models are so similar to types in languages like Java, C# and TypeScript. Using these models, we can pass untrusted data and pydantic will parse as well as validate the data to check if the fields the data has conform to the fields defined on our models.

Let us create our first pydantic model. If you installed `fastapi`, you already installed pydantc. So let's us create a file called `schemas.py` where we shall create our models. A model in Pydantic is created by inheriting from the `Base` class. Let us create a simple model like this.

```python
from pydantic import BaseModel
import uuid

def create_id():
    return uuid.uuid4()


class User(BaseModel):
    id: str = str(create_id())
    username: str
    email: str
```
