from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Load data
with open("data.json") as f:
    data = json.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/api/search")
async def search(q: str):
    results = []
    for item in data:
        if q.lower() in item["title"].lower() or q.lower() in item["description"].lower():
            results.append(item)
    return JSONResponse(content=results)
  
