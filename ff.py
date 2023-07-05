from fastapi import FastAPI

app = FastAPI()

def get_data():
    a = {"name":"Aekantha","course":"AI with python"}
    return a
@app.post('/post/api')
async def dummy(data:dict):
    return data
# @app.get('/dummy/api')
# async def return_data():
#     data = get_data()
#     return data