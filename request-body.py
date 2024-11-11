from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int
    # height: Optional[int]
    # heigth: int | None = None
    heigth: Union[int, None] = 0


@app.post('/home/')
def index(prs:Person):
    return prs