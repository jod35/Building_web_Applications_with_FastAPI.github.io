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
```json
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
From the above schema, we see that the name of the schema is `User` and the type is `object`. Let us look at the properties of these schema. We have the `id` which is an integer, `username` which is a string and `email` which is also a string. The schema also shows us the required fields in our schema and those are all the fields (`id`,`username`,`email`). This gives us a really cool description of our schema.  

This example showed us how we can create our schemas using standard types which include `str`,   `int`, `bool`, `float` and so on. Let us add to our code by using some compound data types on our fields.  
We shall begin by adding a list of `interests` to our `User`. To this, we are going to use a compound data type of `List` that is provided to us by the typing module from the Python standard library.  
```python

from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id:int
    username:str
    email:str
    interests:List[str]=[]


user_data={
    "id":1,
    "username":"username123",
    "email":"username@email.com",
    "interests":["coding","basketball"]
}

new_user=User(**user_data)

print(new_user)

```  
If you have noticed, we have added a field of `interests` that is having a value set to an empty list. So when we run the `schema.py` file, we expect to get the following output.  
```
id=1 username='username123' email='username@email.com' interests=['coding', 'basketball']
```  
Congrats, you have added a list as a field to our Pydantic model. What if we added choices to our model. We are going to make use of enums to achieve this. Now we are going to add a field of `roles` to this model. Let us to update our code by adding the folowing code.  
```python

from pydantic import BaseModel
from typing import List
from enum import Enum



class Role(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    TEACHER = "Teacher"

class User(BaseModel):
    id:int
    username:str
    email:str
    interests:List[str]=[]
    role:Role


user_data={
    "id":1,
    "username":"username123",
    "email":"username@email.com",
    "interests":["coding","basketballa"],
    "role":Role.ADMIN
}

new_user=User(**user_data)

print(new_user)
```  
We have created the role class  
```python
from enum import Enum



class Role(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    TEACHER = "Teacher"
```  
This class contains the roles a user should have in our API. There are three choices here, `ADMIN`,`STUDENT` and `TEACHER`. These are created using an `enum`. We then create a field of `role` that has its type as our `Role` class we have defined. Let us see what happens when we run our `schema.py`.  
```
id=1 username='username123' email='username@email.com' interests=['coding', 'basketballa'] role=<Role.ADMIN: 'Admin'>
```
Our role field has a type that is defned by the `Role` class we have created. In this case our role for the created user is the "ADMIN" role. 

## Validation Errors
In case we want to see validation errors that may be present when we are validating data using a Pydantic model, we use the `ValidationError` class that allows us to see our errors in a very user-friendly way. Let us try it out. Change the code for validating the user data by adding the following.  
```python
# dont forget to import ValidationError
from pydantic import ValidationError

try:
    user_data={
        "id":1,
        "username":"username123",
        "email":"username@email.com",
        "interests":["coding","basketballa"],
        "role":Role.ADMIN
    }

    new_user=User(**user_data)

    print(new_user)

except ValidationError as error:
    print(error)
 
```  
What we are doing here is to check for any validation errors that we may have when validating data using our model. We try to pass our user through the model and if we have any errors, `ValidationError` will return those errors.  
Let us try validating with bad data. So let us change our data.  

```python
try:
    user_data={
        "id":1,
        "username":"username123",
        "email":"username@email.com",
        "interests":"CODING",
        "role":"USER"
    }

    new_user=User(**user_data)

    print(new_user)

except ValidationError as error:
    print(error)
```  
when we run our `schema.py`, we now have the following output. This shows us the errors we have on the fields of `interests` and `role` as shown below.  
```
pydantic.error_wrappers.ValidationError: 2 validation errors for User
interests
  value is not a valid list (type=type_error.list)
role
  value is not a valid enumeration member; permitted: 'Admin', 'Student', 'Teacher' (type=type_error.enum; enum_values=[<Role.ADMIN: 'Admin'>, <Role.STUDENT: 'Student'>, <Role.TEACHER: 'Teacher'>])
```  
 
We can also print this error in a simple easy JSON format by printing `error.json()`. This will give the following output.  
```json
[
  {
    "loc": [
      "interests"
    ],
    "msg": "value is not a valid list",
    "type": "type_error.list"
  },
  {
    "loc": [
      "role"
    ],
    "msg": "value is not a valid enumeration member; permitted: 'Admin', 'Student', 'Teacher'",
    "type": "type_error.enum",
    "ctx": {
      "enum_values": [
        "Admin",
        "Student",
        "Teacher"
      ]
    }
  }
]
```


