from typing import List
from pydantic import BaseModel, validator


class Model(BaseModel):
    values: List[int]

    @validator("values", pre=True)
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(", ")
        return v


if __name__ == "__main__":
    m = Model(values="1, 2, 3")
    print(m.values)