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

