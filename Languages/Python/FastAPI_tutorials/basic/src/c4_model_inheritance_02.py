from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str
    content: str


class PostPublic(PostCreate):
    id: int


class PostDB(PostPublic):
    nb_views: int = 0