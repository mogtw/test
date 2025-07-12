from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/pricing")
def pricing():
    return [{"name": "test", "pricing": 1.1}]