from fastapi import FastAPI, Optional, Cookie


app = FastAPI()


@app.get("/")
async def get_cookie(hello: Optional[str]=Cookie(None)):
    return {"hello": hello}