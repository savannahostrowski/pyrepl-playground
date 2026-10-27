from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(docs_url=None, redoc_url=None)
root = Path(__file__).parent


@app.get("/script.py")
async def script():
    content = (root / "templates" / "script.py").read_text()
    return PlainTextResponse(content)


app.mount("/", StaticFiles(directory=root / "static", html=True), name="website")
