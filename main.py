from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    address: str
    city: str
    pincode: int


class User(BaseModel):
    name: str
    age: int
    address: Address


@app.get('/')
def hello():
    return 'Hello World'


@app.post('/create-user')
def create_user(user: User):
    return {
        'message': 'user created',
        'data': user
    }
