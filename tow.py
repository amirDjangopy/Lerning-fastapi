from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "Hello amirabbas my user"