from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import json

app = FastAPI()

# Serve static files (CSS, JS, Images if any)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set templates folder
templates = Jinja2Templates(directory="templates")

# Load data from JSON
with open("data.json") as f:
    data = json.load(f)

# Home route - serves the search page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

# API route for search
@app.get("/api/search")
async def search(q: str):
    results = []
    for item in data:
        if q.lower() in item["title"].lower() or q.lower() in item["description"].lower():
            results.append(item)
    return JSONResponse(content=results)
    
