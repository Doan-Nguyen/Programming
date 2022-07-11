from fastapi import FastAPI, Response, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


#
app = FastAPI()

#       dummy database 
posts = {
    1: Post(title="Response_1", nb_views=100),
    2: Post(title="Response_2", nb_views=150),
}


#
@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]