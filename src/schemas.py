from pydantic import BaseModel, ValidationError, Field
from typing import List
from enum import Enum


class Role(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    TEACHER = "Teacher"


class User(BaseModel):
    id: int = Field(gt=0)
    username: str = Field(min_length=4, max_length=8)
    email: str = Field(default=None, max_length=80)
    interests: List[str] = []
    role: Role


try:
    user_data = {
        "id": 1,
        "username": "username123",
        "email": "username@email.com",
        "interests": ["coding", "basketballa"],
        "role": Role.ADMIN,
    }

    new_user = User(**user_data)

    print(new_user)

except ValidationError as e:
    print(e.json())
