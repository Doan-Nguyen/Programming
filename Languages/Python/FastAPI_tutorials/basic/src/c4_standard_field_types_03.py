from datetime import date
from typing import List
from pydantic import BaseModel
from c4_standard_field_types_02 import Gender

class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address

    def name_dict(self):
        return self.dict(include={"first_name", "last_name"})