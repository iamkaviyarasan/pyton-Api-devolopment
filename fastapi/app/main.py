
from typing import Optional,List
from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session


 
from .database import engine,get_db
from . import models,schemas,utils
from fastapi import Depends
from .routers import post,user


models.Base.metadata.create_all(bind=engine)


app = FastAPI() 





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
        
    
app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"Hello": "wecome to my api..."} 




