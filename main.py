from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

@app.get("/script.py")
async def script():
    content = (Path(__file__).parent / "templates" / "script.py").read_text()
    return PlainTextResponse(content)
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")
