from fastapi import FastAPI
import os

NAME = os.environ.get("Name", "Docker")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Docker!"}

@app.get("/greet")
def greet():
    return {"Hello": f"{NAME}!!!"}