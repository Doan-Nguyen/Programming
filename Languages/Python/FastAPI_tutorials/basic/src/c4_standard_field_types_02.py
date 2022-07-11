from datetime import date
from enum import Enum
from typing import List
from pydantic import BaseModel


class Gender(str, Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    NON_BINARY = "NON_BINARY"


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]

