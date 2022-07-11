from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str 
    nb_views: int 


app = FastAPI()


#       Dummy database
posts = {
    1: Post(title="Blog", nb_views=95),
    10: Post(title="Video", nb_views=1000),
}

#
@app.get("/posts/{id}")
async def get_post(id: int):
    return posts[id]