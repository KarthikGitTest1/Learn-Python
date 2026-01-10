from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your Python API is working!"}

@app.get("/hello/{name}")
def hello_user(name: str):
    return {"message": f"Hello {name}!"}



class Numbers(BaseModel):
    a: int
    b: int

@app.post("/add")
def add_numbers(values: Numbers):
    return {"result": values.a + values.b}