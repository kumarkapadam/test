

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def msg():
    return "hello welcome"


@app.get("/{name}")
def display_name(name):
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run(app, port=6789)
