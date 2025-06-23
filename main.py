from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello DevOps</title>
    </head>
    <body>
        <h1>Hello DevOps</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
