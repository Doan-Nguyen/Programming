from fastapi import FastAPI, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str


app = FastAPI()

#           dummy database
posts = {
    1: Post(title="Test response", nb_views=100),
}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None