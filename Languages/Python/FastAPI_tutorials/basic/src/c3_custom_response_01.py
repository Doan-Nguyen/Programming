from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse

app = FastAPI()


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Hello kity, mèo méo meo mèo meo !</title>
            </head>
            <body>
                <h1>Pink kity</h1>
            </body>
        </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Olleh"