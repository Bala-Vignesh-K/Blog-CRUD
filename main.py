from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn 

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# the decorator here is used to return the function
# but in angular, it is used for declaration 
# like the @Component that helps in the declaration of "selector" and so on
@app.get('/blog')
def index(limit = 10, published: bool = True, sort: Optional[str]= None):
    if published:
        return {'data': f'{limit} published blogs available in the database'}
    else:
        return {'data':f'{limit} blogs available in the databse'}


# Always add static routing before the dynamic routing
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'Unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog Created with title {blog.title}'}







if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 3000)
