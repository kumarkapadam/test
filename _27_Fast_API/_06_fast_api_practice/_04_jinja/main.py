from urllib.request import Request

from fastapi import FastAPI, Request
import uvicorn
from fastapi.templating import jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = jinja2Templates()


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name: str):
    return templates.TemplateResponse("home.html", {"request": request,
                                                    "username": user_name})


@app.get("/")
def home():
    return "hello welcome to jinja templates"


if __name__ == "__main__":
    uvicorn.run(app, port=5678)
