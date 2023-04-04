from pydantic import BaseModel
from typing import List, Union

class Blog(BaseModel):
    title: str
    body: str

    class Config():
            orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blog: List[Blog] = []
    
    class Config():
            orm_mode = True



class ShowBlog(Blog):
    title: str
    body: str

    creator: ShowUser



class login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None