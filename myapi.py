from fastapi import  FastAPI, Path
from typing import Optional

from fastapi.params import Body
from random import randrange


# schema validation
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content:str
    publish: bool = True
    rating:Optional[int] = None


my_post = []

@app.get('/')
def root():
    return {
        "status":"succes"
    }
   
@app.get('/posts')
def get_post():
    return {
        "status":my_post
    } 

        
@app.post("/posts")
def create_post (post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    my_post.append(post_dict)
    return {
        "status":post_dict
    }
    
    
def find_post(id):
    for p in my_post:
        if p['id']==id:
            return p

@app.get("/posts/latest")
def get_latest_post():
    post = my_post[len(my_post)-1]
    return{
        "latest post":post
    }
 
    
@app.get("/posts/{id}")
def get_post(id:int):
    print("hi")
    post = find_post(id)
    print("hi")
    return {
        "post_details":post
    }
    
