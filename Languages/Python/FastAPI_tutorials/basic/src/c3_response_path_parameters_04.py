from fastapi import FastAPI
from pydantic import BaseModel


class PublicPost(BaseModel):
    title: str 


#       Dummy database
posts = {
    1: PublicPost(title="Blog"),
    10: PublicPost(title="Video"),
}


app = FastAPI()


@app.get("/posts/{id}", response_model=PublicPost)
async def get_posts(id: int):
    return posts[id]