from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Users(BaseModel):
    name: str 
    age: int


class Company(BaseModel):
    name: str
    code: str



@app.post("/users")
async def create_users(user: Users, company: Company):
    return {"user": user, "company": company}
