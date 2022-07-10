from fastapi import FastAPI


app = FastAPI()


@app.post("/users")
async def create_users(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}