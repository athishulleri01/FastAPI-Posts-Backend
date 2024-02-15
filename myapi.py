from fastapi import  FastAPI, HTTPException, Path,Response,status
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
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {
        "post_details":post
    }
    
    
def find_index_post(id):
    for i, p in enumerate(my_post):
        if p['id']==id:
            return i    
    
@app.delete("/posts/{id}")
def delete_post(id:int):
    index = find_index_post(id)
    my_post.pop(index)
    return{
        "message":"Successfully deleted"
    }
    
    
@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    print(post)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    my_post[index] = post_dict
    post_dict['id'] = id
    
    return {
        "message":"Successfully updated"
    }