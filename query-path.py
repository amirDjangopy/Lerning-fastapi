from fastapi import FastAPI, Path, Query
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age:int = Path(ge=0, le=100)
    height: Union[int, None] = 0
    
@app.post('/home/')
async def home(person: Person, car:str=Query('nothing', min_length=2, max_length=20)):
    return person, car