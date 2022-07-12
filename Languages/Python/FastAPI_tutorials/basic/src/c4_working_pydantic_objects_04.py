from pydantic import BaseModel
from c4_model_inheritance_01 import PostCreate, PostPublic, PostDB
from fastapi import FastAPI, status


app = FastAPI()


@app.post("/post",
          status_code=status.HTTP_201_CREATED,
          response_model=PostPublic)
async def create(post_create: PostCreate):
    new_id = max()
