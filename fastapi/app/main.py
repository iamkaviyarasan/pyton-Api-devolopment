from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange



app = FastAPI()


class post(BaseModel):
    title:str
    content:str
    published:bool = True
    rating: Optional[int] =None


my_posts = [{"title": "title of post 1", "content": "content of post 1","id": 1},{"title": "favorite foods","content": "i like pizza","id": 2} ]

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
    

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p    

@app.get("/")
def root():
    return {"Hello": "wecome to my api..."} 

@app.get("/posts")  
def get_post():
    return {"data": my_posts} 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post:post): 
   post_model_dump = post.model_dump()
   post_model_dump ['id'] =randrange(0,100000)
   my_posts.append(post_model_dump)
   return {"data":post_model_dump}


@app.get("/posts/{id}")
def get_post(id: int,response:Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")  
    return {"post_detail":post}

@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #deleting post
    #find the index in the array that has required ID
    #my_posts.pop(index)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_dict = post.model_dump()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data":post_dict}