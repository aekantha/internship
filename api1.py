from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    integer1: int
    integer2: int

@app.post('/add')
def add_numbers(numbers: Numbers):
    result = numbers.integer1 + numbers.integer2
    return {'result': result}