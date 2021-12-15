from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def message():
    return "hello welcome to fastapi"


@app.post("/{name}")
async def message(name):
    return "hello welcome to fastapi", {name}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app)
