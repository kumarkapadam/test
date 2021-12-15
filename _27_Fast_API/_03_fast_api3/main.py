from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def message():
    return "hello welcome to fastapi"

@app.get("/comp/{comp_id}")
async def get_comp(comp_id:int):
    return {"comp_id":comp_id}

@app.get("/comp/")
async def read_comp(num:int,text:str):
    return {"number":num,"text":text}

if __name__ =="__main__":
    uvicorn.run(app)

