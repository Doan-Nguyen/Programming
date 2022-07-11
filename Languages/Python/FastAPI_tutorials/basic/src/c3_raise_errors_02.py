from fastapi import FastAPI, status, Body, HTTPException

app = FastAPI()


@app.post("/password")
async def check_password(password: str = Body(...), 
                         password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail={
                                "message": "Passwords don't match.",
                                "hints": [
                                    "Check the caps lock",
                                ],
                            },
                            )
    return {"massage": "Passwords match"}                            
    