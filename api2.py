from fastapi import FastAPI

app = FastAPI()

def get_data():
    details =  {"Candidate name":"Aekantha",
          "Candidate register_number":"233",
          "Candidate course":"AI with python",
          "Candidate mobile_number":3999939,
          "Candidate address":"884/599,Thilak nagar"
         }
    return details
# @app.post('/post/api')
# async def dummy(data:dict):
#     return data
@app.get('/dummy/api')
async def return_data():
    data = get_data()
    return data
 
# Candidate name
# Candidate register number
# Candidate course
# Candidate mobile number
# Candidate address



