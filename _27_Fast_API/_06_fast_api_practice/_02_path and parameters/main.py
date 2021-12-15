from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()


@app.get("/")
def msg():
    return "hello welcome"


@app.post("/")
def msg():
    return "hello welcome"


@app.post("/")
def msg():
    return "hello welcome"


@app.get("/det/{name}")
def stu_det(name):
    return {"name": name}


@app.get("/comp/{comp_id}")
def component(comp_id):
    return {"component": comp_id}


@app.get("/comp/{id}")  # path parameters
def component(id: int):
    return {"component": id}


@app.get("/student_details/")
def stu_det(name=str, age=int, addr=str):  # query parameters
    return {"name": name, "age": age, "addr": addr}



#optional

@app.get("/student_details/")
def stu_det(name=str, age=Optional[int], addr=str):  # query parameters
    return {"name": name, "age": age, "addr": addr}


if __name__ == "__main__":
    uvicorn.run(app, port=5678)
