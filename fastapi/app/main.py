
from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session


 
from .database import engine,get_db
from . import models
from fastapi import Depends
 
models.Base.metadata.create_all(bind=engine)


app = FastAPI()




class post(BaseModel):
    title:str
    content:str
    published:bool = True
    
while True:
    try:
     conn = psycopg2.connect(
        host='localhost',
        database='fastapi',
        user='postgres',
        password='password',
        cursor_factory=RealDictCursor)
     cursor = conn.cursor() 
     print("Database connection was successful")
     break
    except Exception as error:
     print("Connection to database failed")
     print("Error:", error) 
     time.sleep(2)

    


my_posts = [{"title": "title of post 1", "content": "content of post 1","id": 1},{"title": "favorite foods","content": "i like pizza","id": 2} ]

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
    
   

@app.get("/")
def root():
    return {"Hello": "wecome to my api..."} 

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    posts= db.query(models.Post).all()
    
    print(posts)
    return {"data": "sucessfull"}

@app.get("/posts")   
def get_posts(db: Session = Depends(get_db)):
    # posts = cursor.execute("""SELECT * FROM posts""")
    # posts= cursor.fetchall()
    posts= db.query(models.Post).all()
    return {"data": posts} 

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:post,db: Session = Depends(get_db)): 
  
#   cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#   new_post = cursor.fetchone()
#   conn.commit()
  
  new_post= models.Post(**post.model_dump())
  db.add(new_post)  
  db.commit()
  db.refresh(new_post)
  return {"data":new_post}

@app.get("/posts/{id}")
def get_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str (id),))
    # post =cursor.fetchone()
    post =db.query(models.Post).filter(models.Post.id == id).first ()
    print(post)
   
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")  
    return {"post_detail":post}

@app.delete("/posts/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str (id),))
    # delete_post= cursor.fetchone()
    # conn.commit()
    post =db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)  
    db.commit()

   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post:post,db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str (id), ))
    # update_post=cursor.fetchone()
    # conn.commit()
    post_query =db.query(models.Post).filter(models.Post.id == id)
    postt =post_query.first()
    if postt == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
   
    return {"data":post_query.first()} 