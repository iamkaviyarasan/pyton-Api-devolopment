

from app import oauth2
from .. import models, schemas 
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from typing import Optional,List
from ..database import engine,get_db





router = APIRouter(
    prefix="/posts",
    tags=['Posts']  # this is the tag for the API documentation, this is optional, but it is good to have it.
    # this is the tag for the API documentation, this is optional, but it is good to have it.
    # this is the tag for the API documentation, this is optional, but it is good to have it.
    # this is the tag for the API documentation, this is optional, but it is good to have it."
)



@router.get("/",response_model=List[schemas.Post])   
def get_posts(db: Session = Depends(get_db),user_id: int= Depends(oauth2.get_current_user)): 
    # posts = cursor.execute("""SELECT * FROM posts""")
    # posts= cursor.fetchall()
    posts= db.query(models.Post).all()
    return posts 

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),user_id: int= Depends(oauth2.get_current_user),):

  
#   cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#   new_post = cursor.fetchone()
#   conn.commit()
  print(user_id)
  new_post= models.Post(**post.model_dump())
  db.add(new_post)  
  db.commit()
  db.refresh(new_post)
  return new_post

@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int,db: Session = Depends(get_db),user_id: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str (id),))
    # post =cursor.fetchone()
  post =db.query(models.Post).filter(models.Post.id == id).first ()
    
   
  if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")  
  return post

@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),user_id: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (str (id),))
    # delete_post= cursor.fetchone()
    # conn.commit()
    post =db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)  
    db.commit()

   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db: Session = Depends(get_db),user_id: int= Depends(oauth2.get_current_user)):
    post_query =db.query(models.Post).filter(models.Post.id == id)
    post =post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist") 
   
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    
    db.commit()
   
    
   
    return post