from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    username: str
    email: str
    password: str


class UserOutput(BaseModel):
    username: str
    email: str
    

@app.post('/user/', response_model=UserOutput, status_code=status.HTTP_201_CREATED)
def index(user: UserInput):
    if user.username == 'admin':
        raise HTTPException(detail="username cant be admin", status_code=status.HTTP_400_BAD_REQUEST)
        
    return user