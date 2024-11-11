from fastapi import FastAPI

app = FastAPI()

@app.get('/home/{name}/{age}')
def index(name:str , age:int):
    return {'mesages' : f'Hello {name} is {age} years old.  '}