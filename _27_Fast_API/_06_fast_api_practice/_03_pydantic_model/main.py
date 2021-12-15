from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# from typing import Optional

app = FastAPI()


class Package(BaseModel):
    name: str
    age: str
    addr: str


@app.post("/package/")
def student_details(package: Package):
    return package


@app.post("/package/{priority}")
def student_details(priority: int, package: Package, value=bool):
    return {"priority": priority, **package.dict(), "value": value}


@app.get("/")
def msg():
    return "hello welcome"


if __name__ == "__main__":
    uvicorn.run(app, port=56789)
