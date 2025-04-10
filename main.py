from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

with open("app/data.json") as f:
    data = json.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/api/search")
async def search(q: str):
    results = [item for item in data if q.lower() in item["title"].lower() or q.lower() in item["description"].lower()]
    return JSONResponse(content=results)