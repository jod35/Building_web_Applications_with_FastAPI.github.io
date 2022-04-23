# Managing Pydantic models with FastAPI

In the previous post, we looked at how we could require to provide the request body by using the `Body` function. We looked at how this can give us verbose request handler functions. In this case, we create Pydantic models to help us do our validations.

## What is Pydantic?

[Pydantic](https://pydantic-docs.helpmanual.io/) is the underlying data validation library used in FastAPI. It is a handy data parsing and validation library. It uses type hints to convert input types to the defined type, collects all errors with ValidationError, and is properly documented, making it easy to find.

## Creating Models

Using Pydantic, we can primarily describe our data as `models`. These models are so similar to types in languages like Java, C# and TypeScript. Using these models, we can pass untrusted data and pydantic will parse as well as validate the data to check if the fields the data has conform to the fields defined on our models.

Let us create our first pydantic model. If you installed `fastapi`, you already installed pydantc. So let's us create a file called `schemas.py` where we shall create our models. A model in Pydantic is created by inheriting from the `BaseModel` class. Let us create a simple model like this.

```python
from pydantic import BaseModel


class User(BaseModel):
    id: str 
    username: str
    email: str
```  
We have created a class of `User` which inherits from `BaseModel`. This is our pydantic model which defines our fields using type annotations.  

### What's really happening here?
- We are creating a field of `id` which is of type `str`. The type-only annotation means that this field is required. 
- We also have a `username` field which is of type `str`
- We also have an `email` field which is of type `str`  

All of the fields defined on our model are required and have the `str` type. Now let us create a user. 
```python

from pydantic import BaseModel


class User(BaseModel):
    id:int
    username:str
    email:str


user_data={
    "id":1,
    "username":"username123",
    "email":"username@email.com"
}

new_user=User(**user_data)

print(new_user)
```  

When we run `schemas.py`, this will give us the string representation of the `User` object as shown below. 
```
id=1 username='username123' email='username@email.com'
```  
We can also do things like printing the user as a dictionary.  
```python
print(new_user.dict())
```  
This will give us the data of user as a Python dictionary. Printing the user as JSON will be.  
```python
print(new_user.json())
```  

If we want to find out about the `User` schema, we then have to add the following code.  
```python
print(new_user.schema())
```  
This will give the output below which is untidy.  
```
{"title": "User", "type": "object", "properties": {"id": {"title": "Id", "type": "integer"}, "username": {"title": "Username", "type": "string"}, "email": {"title": "Email", "type": "string"}}, "required": ["id", "username", "email"]}
```  
Let us the `json` Python module to help us to organize this schema with some indentation. So let us do this with  
```python
import json

dict_schema=new_user.schema()

print(json.dump(dict_schema,indent=4))

```
This gives us the following output.  
```
{
    "title": "User",
    "type": "object",
    "properties": {
        "id": {
            "title": "Id",
            "type": "integer"
        },
        "username": {
            "title": "Username",
            "type": "string"
        },
        "email": {
            "title": "Email",
            "type": "string"
        }
    },
    "required": [
        "id",
        "username",
        "email"
    ]
}
```  
From the above schema, we see that the name of the schema is `User` and the type is `object`. Let us lokk at the properties of these schema. We have the `id` which is an integer, `username` which is a string and `email` which is also a string. The schema also shows us the required fields in our schema and those are all the fields (`id`,`username`,`email`).

