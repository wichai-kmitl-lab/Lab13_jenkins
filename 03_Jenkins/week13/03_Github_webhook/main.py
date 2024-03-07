# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Welcome to Jenkin Webhook using Fastapi </h1>
            <h1>Welcome to Wichai in my Devtools </h1>
            <h1>Welcome to Wichai in my Devtools </h1>
            <h1>Welcome to Wichai in my Devtools </h1>
        </body>
    </html>
    """
